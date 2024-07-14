@echo off

for %%I in (.) do set currentFolder=%%~nxI
chcp 65001 > nul
echo.
echo Activando el entorno virtual
call venv/Scripts/activate
echo Entorno virtual activado con éxito
echo Listando los módulos instalados en %currentFolder%...
echo. 
pip list
echo.
echo Creando el archivo requirements.txt...
pip freeze > requirements.txt
echo requirements.txt creado con éxito
echo.
pause