#Requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string] $Url,

    [Parameter(Mandatory = $false)]
    [string] $OutputPath,

    [Parameter(Mandatory = $false)]
    [ValidateSet("json", "markdown", "both")]
    [string] $Format = "both",

    [Parameter(Mandatory = $false)]
    [string] $HtmlPath
)

$ErrorActionPreference = "Stop"

function Get-MobalyticsBuildUrlParts {
    param(
        [Parameter(Mandatory = $true)]
        [string] $BuildUrl
    )

    $normalizedUrl = $BuildUrl.Trim().TrimEnd("/")

    if ($normalizedUrl -notmatch "mobalytics\.gg/poe-2/profile/([^/]+)/builds/([^/?#]+)") {
        throw "URL invalida. Esperado: https://mobalytics.gg/poe-2/profile/{author}/builds/{slug}"
    }

    return @{
        AuthorProfileName = $Matches[1]
        SlugifiedName     = $Matches[2]
    }
}

function Get-MobalyticsBuildPageHtml {
    param(
        [Parameter(Mandatory = $true)]
        [string] $BuildUrl
    )

    $tempHtmlPath = Join-Path ([System.IO.Path]::GetTempPath()) "mobalytics_build_$([Guid]::NewGuid().ToString()).html"
    $userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

    try {
        $curlOutput = & curl.exe -sL `
            -A $userAgent `
            -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" `
            -H "Accept-Language: en-US,en;q=0.9" `
            --max-time 120 `
            -o $tempHtmlPath `
            -w "%{http_code}" `
            $BuildUrl

        if ($LASTEXITCODE -ne 0) {
            throw "curl.exe falhou com codigo $LASTEXITCODE."
        }

        $httpStatusCode = [int]$curlOutput

        if ($httpStatusCode -ne 200) {
            throw "Falha ao baixar a pagina. HTTP $httpStatusCode"
        }

        $htmlContent = Get-Content -Path $tempHtmlPath -Raw -Encoding UTF8

        $hasCloudflareChallenge = $htmlContent -match "Just a moment|Enable JavaScript and cookies"
        $hasBuildData = $htmlContent -match '"buildVariants"'

        if ($hasCloudflareChallenge -and -not $hasBuildData) {
            throw "Pagina bloqueada pelo Cloudflare. Tente novamente ou abra a URL no navegador e salve o HTML localmente."
        }

        if (-not $hasBuildData) {
            throw "Dados do build nao encontrados na pagina baixada."
        }

        return $htmlContent
    }
    finally {
        Remove-Item -Path $tempHtmlPath -Force -ErrorAction SilentlyContinue
    }
}

function ConvertFrom-MobalyticsEscapedJson {
    param(
        [Parameter(Mandatory = $true)]
        [string] $JsonText
    )

    $decodedText = $JsonText -replace "\\u002F", "/"

    return $decodedText | ConvertFrom-Json -Depth 100
}

function Get-MobalyticsJsonBlock {
    param(
        [Parameter(Mandatory = $true)]
        [string] $HtmlContent,

        [Parameter(Mandatory = $true)]
        [string] $PropertyName
    )

    $searchToken = "`"$PropertyName`":"
    $startIndex = $HtmlContent.IndexOf($searchToken)

    if ($startIndex -lt 0) {
        throw "Dados do build nao encontrados na pagina (propriedade '$PropertyName')."
    }

    $braceStart = $HtmlContent.IndexOf("{", $startIndex)

    if ($braceStart -lt 0) {
        throw "JSON de '$PropertyName' malformado."
    }

    $depth = 0
    $endIndex = $braceStart

    for ($index = $braceStart; $index -lt $HtmlContent.Length; $index++) {
        $character = $HtmlContent[$index]

        if ($character -eq "{") {
            $depth++
        }
        elseif ($character -eq "}") {
            $depth--

            if ($depth -eq 0) {
                $endIndex = $index + 1
                break
            }
        }
    }

    if ($depth -ne 0) {
        throw "JSON de '$PropertyName' incompleto na pagina."
    }

    $length = $endIndex - $braceStart

    return $HtmlContent.Substring($braceStart, $length)
}

function Get-MobalyticsActVariantMapping {
    param(
        [Parameter(Mandatory = $true)]
        [string] $HtmlContent
    )

    $mapping = [ordered]@{}
    $pattern = 'id="react-aria[^"]*-tab-([0-9a-f-]{36})"[^>]*>.*?x1psj106">([^<]+)<'
    $matches = [regex]::Matches($HtmlContent, $pattern)

    foreach ($match in $matches) {
        $variantId = $match.Groups[1].Value
        $actLabel = $match.Groups[2].Value.Trim()

        if (-not $mapping.Contains($variantId)) {
            $mapping[$variantId] = $actLabel
        }
    }

    return $mapping
}

function Get-MobalyticsBuildTitle {
    param(
        [Parameter(Mandatory = $true)]
        [string] $HtmlContent
    )

    if ($HtmlContent -match '"name":"([^"]+)\s*-\s*PoE 2') {
        return $Matches[1].Trim()
    }

    if ($HtmlContent -match '<title>([^<]+)</title>') {
        $title = $Matches[1].Trim()
        $title = $title -replace "\s*[-|]\s*PoE 2.*$", ""
        $title = $title -replace "\s*[-|]\s*Mobalytics.*$", ""

        if (-not [string]::IsNullOrWhiteSpace($title)) {
            return $title
        }
    }

    return "Mobalytics Build"
}

function Get-MobalyticsEquipmentEntries {
    param(
        $EquipmentObject
    )

    $entries = [System.Collections.Generic.List[object]]::new()

    if ($null -eq $EquipmentObject) {
        return $entries
    }

    $simpleSlots = @(
        "amulet", "belt", "body", "boots", "flask1", "flask2",
        "charm1", "charm2", "charm3", "gloves", "helmet",
        "leftRing", "extraRing", "rightRing"
    )

    foreach ($slotName in $simpleSlots) {
        $slotValue = $EquipmentObject.$slotName

        if ($null -ne $slotValue) {
            $entries.Add([ordered]@{
                slotType = $slotName
                item     = $slotValue
            })
        }
    }

    foreach ($weaponSlot in @("mainHand", "offHand")) {
        $weaponValue = $EquipmentObject.$weaponSlot

        if ($null -eq $weaponValue) {
            continue
        }

        foreach ($weaponSetName in @("set1", "set2")) {
            $setValue = $weaponValue.$weaponSetName

            if ($null -ne $setValue) {
                $entries.Add([ordered]@{
                    slotType = $weaponSlot
                    item     = $setValue
                })
            }
        }
    }

    return $entries
}

function Get-MobalyticsEquipmentItemForPriority {
    param(
        $EquipmentObject,
        $PriorityItem
    )

    $entries = Get-MobalyticsEquipmentEntries -EquipmentObject $EquipmentObject
    $prioritySlug = $PriorityItem.slug

    foreach ($entry in $entries) {
        $commonItem = $entry.item.commonItem

        if ($null -eq $commonItem) {
            continue
        }

        $slugMatches = $commonItem.slug -eq $prioritySlug
        $nameMatches = $commonItem.name -eq $PriorityItem.name

        if ($slugMatches -or $nameMatches) {
            return $entry.item
        }
    }

    $slotMatches = $entries | Where-Object { $_.slotType -eq $PriorityItem.type }

    if ($slotMatches.Count -gt 0) {
        return $slotMatches[0].item
    }

    return $null
}

function Get-MobalyticsItemModifiers {
    param(
        $ItemObject
    )

    $modifiers = [System.Collections.Generic.List[string]]::new()

    if ($null -eq $ItemObject) {
        return $modifiers
    }

    $commonItem = $ItemObject.commonItem

    if ($null -eq $commonItem) {
        return $modifiers
    }

    if ($null -ne $commonItem.explicitDescriptions) {
        foreach ($description in $commonItem.explicitDescriptions) {
            if (-not [string]::IsNullOrWhiteSpace($description.description)) {
                $modifiers.Add($description.description)
            }
        }
    }

    if ($null -ne $commonItem.implicitDescriptions) {
        foreach ($description in $commonItem.implicitDescriptions) {
            if (-not [string]::IsNullOrWhiteSpace($description.description)) {
                $modifiers.Add($description.description)
            }
        }
    }

    return $modifiers
}

function Get-MobalyticsSupportGemNameMap {
    param(
        $SkillGemsObject
    )

    $nameBySlug = @{}

    if ($null -eq $SkillGemsObject) {
        return $nameBySlug
    }

    if ($null -ne $SkillGemsObject.priorityGems) {
        foreach ($priorityGem in $SkillGemsObject.priorityGems) {
            if (-not [string]::IsNullOrWhiteSpace($priorityGem.gemSlug)) {
                $nameBySlug[$priorityGem.gemSlug] = $priorityGem.name
            }
        }
    }

    if ($null -ne $SkillGemsObject.gems) {
        foreach ($gem in $SkillGemsObject.gems) {
            if ($null -eq $gem.subSkills) {
                continue
            }

            foreach ($subSkill in $gem.subSkills) {
                if (-not [string]::IsNullOrWhiteSpace($subSkill.gemSlug)) {
                    if (-not $nameBySlug.ContainsKey($subSkill.gemSlug)) {
                        $displayName = $subSkill.gemSlug -replace "player$", "" -replace "support", "" -replace "([a-z])([A-Z])", '$1 $2'
                        $nameBySlug[$subSkill.gemSlug] = (Get-Culture).TextInfo.ToTitleCase($displayName.ToLower())
                    }
                }
            }
        }
    }

    return $nameBySlug
}

function Get-MobalyticsSupportGemName {
    param(
        $SubSkillObject,
        [hashtable] $SupportGemNameBySlug
    )

    $gemSlug = $SubSkillObject.gemSlug

    if (-not [string]::IsNullOrWhiteSpace($gemSlug) -and $SupportGemNameBySlug.ContainsKey($gemSlug)) {
        return $SupportGemNameBySlug[$gemSlug]
    }

    return $gemSlug
}

function Get-MobalyticsBuildExport {
    param(
        [Parameter(Mandatory = $true)]
        [string] $HtmlContent,

        [Parameter(Mandatory = $true)]
        [string] $BuildUrl
    )

    $buildVariantsJson = Get-MobalyticsJsonBlock -HtmlContent $HtmlContent -PropertyName "buildVariants"
    $buildVariants = ConvertFrom-MobalyticsEscapedJson -JsonText $buildVariantsJson
    $actMapping = Get-MobalyticsActVariantMapping -HtmlContent $HtmlContent
    $buildTitle = Get-MobalyticsBuildTitle -HtmlContent $HtmlContent
    $urlParts = Get-MobalyticsBuildUrlParts -BuildUrl $BuildUrl

    $acts = [System.Collections.Generic.List[object]]::new()

    foreach ($variant in $buildVariants.values) {
        $variantId = $variant.id
        $actLabel = $actMapping[$variantId]

        if ([string]::IsNullOrWhiteSpace($actLabel)) {
            $actLabel = "Variant $variantId"
        }

        $equipmentItems = [System.Collections.Generic.List[object]]::new()
        $equipmentObject = $variant.equipment

        if ($null -ne $equipmentObject -and $null -ne $equipmentObject.priorityList) {
            foreach ($priorityItem in $equipmentObject.priorityList) {
                $slotType = $priorityItem.type
                $slotObject = Get-MobalyticsEquipmentItemForPriority -EquipmentObject $equipmentObject -PriorityItem $priorityItem
                $modifiers = Get-MobalyticsItemModifiers -ItemObject $slotObject

                $equipmentItems.Add([ordered]@{
                    name      = $priorityItem.name
                    slot      = $slotType
                    slug      = $priorityItem.slug
                    modifiers = @($modifiers)
                })
            }
        }

        $skillGemItems = [System.Collections.Generic.List[object]]::new()
        $skillGemsObject = $variant.skillGems
        $supportGemNameBySlug = Get-MobalyticsSupportGemNameMap -SkillGemsObject $skillGemsObject

        if ($null -ne $skillGemsObject -and $null -ne $skillGemsObject.gems) {
            foreach ($gem in $skillGemsObject.gems) {
                $activeSkill = $gem.activeSkill
                $levelSuffix = ""

                if ($null -ne $activeSkill.level) {
                    $levelSuffix = " (Level $($activeSkill.level))"
                }

                $supportNames = [System.Collections.Generic.List[string]]::new()

                if ($null -ne $gem.subSkills) {
                    foreach ($subSkill in $gem.subSkills) {
                        $supportNames.Add((Get-MobalyticsSupportGemName -SubSkillObject $subSkill -SupportGemNameBySlug $supportGemNameBySlug))
                    }
                }

                $skillGemItems.Add([ordered]@{
                    name     = "$($activeSkill.name)$levelSuffix"
                    slug     = $activeSkill.gemSlug
                    supports = @($supportNames)
                })
            }
        }

        $passiveNodes = [System.Collections.Generic.List[object]]::new()
        $passiveTreeObject = $variant.passiveTree

        if ($null -ne $passiveTreeObject) {
            if ($null -ne $passiveTreeObject.mainTree -and $null -ne $passiveTreeObject.mainTree.priorityList) {
                foreach ($node in $passiveTreeObject.mainTree.priorityList) {
                    $passiveNodes.Add([ordered]@{
                        name = $node.name
                        slug = $node.slug
                        tree = "main"
                    })
                }
            }

            if ($null -ne $passiveTreeObject.ascendancyTree -and $null -ne $passiveTreeObject.ascendancyTree.priorityList) {
                foreach ($node in $passiveTreeObject.ascendancyTree.priorityList) {
                    $passiveNodes.Add([ordered]@{
                        name = $node.name
                        slug = $node.slug
                        tree = "ascendancy"
                    })
                }
            }
        }

        $acts.Add([ordered]@{
            act          = $actLabel
            variantId    = $variantId
            equipment    = @($equipmentItems)
            skillGems    = @($skillGemItems)
            passiveTree  = @($passiveNodes)
        })
    }

    return [ordered]@{
        sourceUrl = $BuildUrl
        buildName = $buildTitle
        author    = $urlParts.AuthorProfileName
        slug      = $urlParts.SlugifiedName
        acts      = @($acts)
    }
}

function ConvertTo-MobalyticsBuildMarkdown {
    param(
        [Parameter(Mandatory = $true)]
        $BuildExport
    )

    $lines = [System.Collections.Generic.List[string]]::new()
    $lines.Add("# $($BuildExport.buildName)")
    $lines.Add("")
    $lines.Add("Fonte: [$($BuildExport.sourceUrl)]($($BuildExport.sourceUrl))")
    $lines.Add("Autor: $($BuildExport.author)")
    $lines.Add("")

    foreach ($act in $BuildExport.acts) {
        $lines.Add("## $($act.act)")
        $lines.Add("")

        $lines.Add("### Equipment")
        $lines.Add("")

        foreach ($item in $act.equipment) {
            $lines.Add("- [ ] $($item.name)")

            foreach ($modifier in $item.modifiers) {
                $lines.Add("    - [ ] $modifier")
            }

            if ($item.modifiers.Count -eq 0) {
                $lines.Add("    - [ ] _(sem modificadores na pagina)_")
            }
        }

        $lines.Add("")
        $lines.Add("### Skill Gems")
        $lines.Add("")

        foreach ($skillGem in $act.skillGems) {
            $lines.Add("- [ ] $($skillGem.name)")

            foreach ($support in $skillGem.supports) {
                $lines.Add("    - [ ] $support")
            }
        }

        $lines.Add("")
        $lines.Add("### Passive Tree")
        $lines.Add("")

        foreach ($node in $act.passiveTree) {
            $lines.Add("- [ ] $($node.name)")
        }

        $lines.Add("")
        $lines.Add("---")
        $lines.Add("")
    }

    return ($lines -join "`n").TrimEnd() + "`n"
}

$urlParts = Get-MobalyticsBuildUrlParts -BuildUrl $Url
$exportsDirectory = Join-Path (Split-Path -Parent $PSScriptRoot) "Exports"

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    if (-not (Test-Path $exportsDirectory)) {
        New-Item -ItemType Directory -Path $exportsDirectory -Force | Out-Null
    }

    $safeSlug = $urlParts.SlugifiedName -replace '[^\w\-]', '-'
    $OutputPath = Join-Path $exportsDirectory $safeSlug

    if (-not (Test-Path $OutputPath)) {
        New-Item -ItemType Directory -Path $OutputPath -Force | Out-Null
    }
}
else {
    $OutputPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutputPath)
    $isFileOutput = $OutputPath.EndsWith(".json") -or $OutputPath.EndsWith(".md")

    if (-not $isFileOutput) {
        if (-not (Test-Path $OutputPath)) {
            New-Item -ItemType Directory -Path $OutputPath -Force | Out-Null
        }
    }
    else {
        $parentDirectory = Split-Path -Parent $OutputPath

        if (-not [string]::IsNullOrWhiteSpace($parentDirectory) -and -not (Test-Path $parentDirectory)) {
            New-Item -ItemType Directory -Path $parentDirectory -Force | Out-Null
        }
    }
}

if (-not [string]::IsNullOrWhiteSpace($HtmlPath)) {
    $resolvedHtmlPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($HtmlPath)

    if (-not (Test-Path $resolvedHtmlPath)) {
        throw "Arquivo HTML nao encontrado: $resolvedHtmlPath"
    }

    Write-Host "Carregando HTML local: $resolvedHtmlPath"
    $htmlContent = Get-Content -Path $resolvedHtmlPath -Raw -Encoding UTF8
}
else {
    Write-Host "Baixando build de Mobalytics..."
    $htmlContent = Get-MobalyticsBuildPageHtml -BuildUrl $Url
}

Write-Host "Extraindo dados do build..."
$buildExport = Get-MobalyticsBuildExport -HtmlContent $htmlContent -BuildUrl $Url

$jsonOutputPath = $OutputPath
$markdownOutputPath = $OutputPath

if (-not $OutputPath.EndsWith(".json") -and -not $OutputPath.EndsWith(".md")) {
    $jsonOutputPath = Join-Path $OutputPath "$($urlParts.SlugifiedName).json"
    $markdownOutputPath = Join-Path $OutputPath "$($urlParts.SlugifiedName).md"
}
elseif ($OutputPath.EndsWith(".json")) {
    $markdownOutputPath = $OutputPath -replace '\.json$', '.md'
}
elseif ($OutputPath.EndsWith(".md")) {
    $jsonOutputPath = $OutputPath -replace '\.md$', '.json'
}

$shouldWriteJson = $Format -eq "json" -or $Format -eq "both"
$shouldWriteMarkdown = $Format -eq "markdown" -or $Format -eq "both"

if ($shouldWriteJson) {
    $buildExport | ConvertTo-Json -Depth 20 | Set-Content -Path $jsonOutputPath -Encoding UTF8
    Write-Host "JSON: $jsonOutputPath"
}

if ($shouldWriteMarkdown) {
    $markdownContent = ConvertTo-MobalyticsBuildMarkdown -BuildExport $buildExport
    Set-Content -Path $markdownOutputPath -Value $markdownContent -Encoding UTF8 -NoNewline
    Write-Host "Markdown: $markdownOutputPath"
}

Write-Host ""
Write-Host "Build: $($buildExport.buildName)"
Write-Host "Acts: $($buildExport.acts.Count)"

foreach ($act in $buildExport.acts) {
    Write-Host "  - $($act.act): $($act.equipment.Count) equipment, $($act.skillGems.Count) gems, $($act.passiveTree.Count) passives"
}
