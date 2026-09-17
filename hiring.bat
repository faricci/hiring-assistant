@echo off
REM Thin wrapper: run the hiring CLI with Python from any cwd.
setlocal
set "DIR=%~dp0"
where py >nul 2>nul && (py "%DIR%hiring.py" %* & exit /b %errorlevel%)
python "%DIR%hiring.py" %*
exit /b %errorlevel%
