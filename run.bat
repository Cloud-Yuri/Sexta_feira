@echo off
cd /d "%~dp0"
call venv312\Scripts\activate
py main.py
pause