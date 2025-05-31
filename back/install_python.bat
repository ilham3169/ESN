@echo off
echo Checking for Python installation...

:: Check if python is installed
python --version >nul 2>&1
if %ERRORLEVEL% == 0 (
    echo Python is already installed.
    goto install_dependencies
)

echo Python not found. Downloading and installing Python...

:: Download Python installer (using PowerShell)
powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile 'python-installer.exe'"

:: Install Python silently
echo Installing Python...
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install Python. Please install it manually from https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Clean up installer
del python-installer.exe
echo Python installed successfully.

:: Install dependencies
:install_dependencies
echo Installing required Python packages...
python -m ensurepip --default-pip
python -m pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install dependencies. Please install them manually using 'pip install -r requirements.txt'.
    pause
    exit /b 1
)
echo Dependencies installed successfully.

:: Run the Python script
:run_script
echo Running WhatsApp script...
python main.py
if %ERRORLEVEL% NEQ 0 (
    echo Failed to run the script. Ensure whatsapp_script.py exists and is correct.
    pause
    exit /b 1
)

pause