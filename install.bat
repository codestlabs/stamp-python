@echo off
echo Installing Stamp for Python...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Install Python 3.10+ first.
    exit /b 1
)
CHOICE /C YN /M "Do you want to upgrade pip?"
IF %ERRORLEVEL%==1 goto y
IF %ERRORLEVEL%==2 goto n
ELSE goto n
:y
python -m pip install --upgrade pip
python -m pip install .
goto end
:n
python -m pip install .
goto end
:end
echo Installation complete.