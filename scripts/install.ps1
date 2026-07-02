param(
    [Parameter(Mandatory = $true)]
    [string]$Target,

    [ValidateSet("claude", "factory", "both")]
    [string]$Platform = "both",

    [switch]$Force
)

$ErrorActionPreference = "Stop"
$SourceDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$TargetDir = (Resolve-Path $Target).Path

function Copy-AgentBuilder {
    param([Parameter(Mandatory = $true)][string]$Destination)

    if (Test-Path $Destination) {
        if (-not $Force) {
            throw "Destination already exists: $Destination. Use -Force to replace it."
        }
        Remove-Item -Recurse -Force $Destination
    }

    New-Item -ItemType Directory -Force $Destination | Out-Null

    Get-ChildItem -Force $SourceDir |
        Where-Object { $_.Name -ne ".git" -and $_.Extension -ne ".zip" } |
        ForEach-Object {
            Copy-Item -Recurse -Force $_.FullName $Destination
        }

    Write-Host "Installed: $Destination"
}

if ($Platform -eq "claude" -or $Platform -eq "both") {
    $ClaudeRoot = Join-Path $TargetDir ".claude\skills"
    New-Item -ItemType Directory -Force $ClaudeRoot | Out-Null
    Copy-AgentBuilder -Destination (Join-Path $ClaudeRoot "agent-builder")
}

if ($Platform -eq "factory" -or $Platform -eq "both") {
    $FactoryRoot = Join-Path $TargetDir ".factory\skills"
    New-Item -ItemType Directory -Force $FactoryRoot | Out-Null
    Copy-AgentBuilder -Destination (Join-Path $FactoryRoot "agent-builder")
}

Write-Host "Installation complete."
