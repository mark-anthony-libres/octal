@echo off

REM Activate the virtual environment
call .\venv\Scripts\activate

REM Run sender.py in the background
echo Running sender.py...
start python sender.py

REM Run receiver.py in the background
echo Running receiver.py...
start python receiver.py

REM Wait for user to press a key to exit
pause

REM Deactivate the virtual environment
deactivate
