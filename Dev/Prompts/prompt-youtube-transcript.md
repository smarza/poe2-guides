# YouTube transcript with timeline

**Video:** https://www.youtube.com/watch?v=s2LkL7ev27Y  
**Video ID:** `s2LkL7ev27Y`

## Status

Could not extract the transcript directly in this environment.

Attempts made:

1. `youtube-transcript-api` in Python.
   - Failed because the execution environment could not resolve/access `www.youtube.com`.
2. Opening the video directly via web tool.
   - Failed because online access to YouTube was limited/throttled.
3. Searching for a publicly indexed copy of the transcript on the web.
   - No publicly indexed transcript was found for this `video_id`.

## How to generate locally with timeline

### Recommended: PowerShell script

From the repo root:

```powershell
.\Dev\Scripts\Export-YouTubeTranscript.ps1 "https://www.youtube.com/watch?v=s2LkL7ev27Y"
```

The file is saved to:

```text
Dev/Transcriptions/transcript_s2LkL7ev27Y_with_timeline.md
```

Optional custom output:

```powershell
.\Dev\Scripts\Export-YouTubeTranscript.ps1 "https://www.youtube.com/watch?v=s2LkL7ev27Y" -OutputPath ".\Dev\Transcriptions\custom_name.md"
```

### Manual Python fallback

Install locally:

```bash
pip install youtube-transcript-api
```

Then use this script:

```python
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "s2LkL7ev27Y"

api = YouTubeTranscriptApi()
transcript = api.fetch(video_id, languages=["pt", "pt-BR", "en"])

def fmt_time(seconds: float) -> str:
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

output_path = "Dev/Transcriptions/transcript_s2LkL7ev27Y_with_timeline.md"

with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Transcript with timeline\n\n")
    f.write("Video: https://www.youtube.com/watch?v=s2LkL7ev27Y\n\n")
    for item in transcript:
        f.write(f"[{fmt_time(item.start)}] {item.text}\n")
```

## Alternative with yt-dlp

```bash
yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "pt.*,en.*" --sub-format vtt "https://www.youtube.com/watch?v=s2LkL7ev27Y"
```

This should generate a `.vtt` file with timestamps if the video has manual or automatic captions available.
