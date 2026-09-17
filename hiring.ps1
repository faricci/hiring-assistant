# Thin wrapper: run the hiring CLI with Python from any cwd.
$ErrorActionPreference = 'Stop'
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = if (Get-Command py -ErrorAction SilentlyContinue) { 'py' } else { 'python' }
& $python (Join-Path $dir 'hiring.py') @args
exit $LASTEXITCODE
