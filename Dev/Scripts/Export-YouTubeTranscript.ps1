[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string] $Url,

    [Parameter(Mandatory = $false)]
    [string] $OutputPath,

    [Parameter(Mandatory = $false)]
    [string[]] $Languages = @("en")
)

function Get-YouTubeVideoId {
    param(
        [Parameter(Mandatory = $true)]
        [string] $YouTubeUrl
    )

    $parsedUrl = $YouTubeUrl.Trim()

    if ($parsedUrl -match 'youtu\.be/([A-Za-z0-9_-]{11})') {
        return $Matches[1]
    }

    if ($parsedUrl -match '[?&]v=([A-Za-z0-9_-]{11})') {
        return $Matches[1]
    }

    if ($parsedUrl -match 'youtube\.com/(?:embed|shorts|live)/([A-Za-z0-9_-]{11})') {
        return $Matches[1]
    }

    if ($parsedUrl -match '^([A-Za-z0-9_-]{11})$') {
        return $parsedUrl
    }

    throw "Could not extract video ID from URL: $YouTubeUrl"
}

function Ensure-YouTubeTranscriptApi {
    python -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('youtube_transcript_api') else 1)" 2>$null

    if ($LASTEXITCODE -ne 0) {
        Write-Host "Installing youtube-transcript-api..."
        python -m pip install youtube-transcript-api

        if ($LASTEXITCODE -ne 0) {
            throw "Failed to install youtube-transcript-api."
        }
    }
}

$videoId = Get-YouTubeVideoId -YouTubeUrl $Url
$watchUrl = "https://www.youtube.com/watch?v=$videoId"
$transcriptionsDirectory = Join-Path (Split-Path -Parent $PSScriptRoot) "Transcriptions"

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    if (-not (Test-Path $transcriptionsDirectory)) {
        New-Item -ItemType Directory -Path $transcriptionsDirectory -Force | Out-Null
    }

    $OutputPath = Join-Path $transcriptionsDirectory "transcript_${videoId}_with_timeline.md"
}
else {
    $OutputPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutputPath)
}

Ensure-YouTubeTranscriptApi

$configJson = (@{
    video_id = $videoId
    output_path = ($OutputPath -replace '\\', '/')
    watch_url = $watchUrl
    languages = @($Languages)
} | ConvertTo-Json -Compress)

$pythonScript = @"
from youtube_transcript_api import YouTubeTranscriptApi
import json

config = json.loads('''$configJson''')

video_id = config["video_id"]
languages = config["languages"]
output_path = config["output_path"]
watch_url = config["watch_url"]

api = YouTubeTranscriptApi()

try:
    transcript = api.fetch(video_id, languages=languages)
except Exception:
    transcript = api.fetch(video_id)

def fmt_time(seconds):
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

with open(output_path, "w", encoding="utf-8") as file:
    file.write("# Transcript with timeline\n\n")
    file.write(f"Video: {watch_url}\n\n")

    for item in transcript:
        file.write(f"[{fmt_time(item.start)}] {item.text}\n")

print(output_path)
"@

$tempScriptPath = Join-Path ([System.IO.Path]::GetTempPath()) "export_youtube_transcript_$([Guid]::NewGuid().ToString()).py"
Set-Content -Path $tempScriptPath -Value $pythonScript -Encoding UTF8

try {
    $result = python $tempScriptPath 2>&1

    if ($LASTEXITCODE -ne 0) {
        throw ($result | Out-String)
    }

    $lineCount = (Get-Content -Path $OutputPath | Measure-Object -Line).Lines

    Write-Host "Transcript exported successfully."
    Write-Host "Video ID: $videoId"
    Write-Host "File: $OutputPath"
    Write-Host "Lines: $lineCount"
}
finally {
    Remove-Item -Path $tempScriptPath -Force -ErrorAction SilentlyContinue
}
