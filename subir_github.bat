@echo off
title Subiendo a GitHub...
color 0b

echo ===================================================
echo     GUARDANDO Y SUBIENDO CAMBIOS A GITHUB
echo ===================================================
echo.

echo [1/3] Preparando archivos modificados...
git add .

echo [2/3] Creando punto de guardado (commit)...
git commit -m "Actualizacion rapida (Autoguardado)"

echo [3/3] Subiendo a la nube (GitHub)...
git push origin main

echo.
echo ===================================================
echo     !LISTO! CAMBIOS SUBIDOS CORRECTAMENTE.
echo ===================================================
timeout /t 4 /nobreak > nul
exit
