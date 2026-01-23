Write-Host "Installing Stamp for Python..."
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python not found. Install Python 3.10+ first."
    exit 1
}
Write-Host "Do you want to updgrade pip? [y/n]: " -NoNewline
$response = Read-Host ""
if ($response -eq "y") {
    python -m pip install --upgrade pip
    python -m pip install .
} elseif ($response -eq "Y") {
    python -m pip install --upgrade pip
    python -m pip install .
} else {
    python -m pip install .   
}
python -m pip install --upgrade pip
python -m pip install .
Write-Host "Installation complete."