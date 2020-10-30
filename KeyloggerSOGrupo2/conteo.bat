@echo off

(for /f "tokens=2,* delims= " %%a in (reporte.txt) do echo %%b) > reporte2.txt
