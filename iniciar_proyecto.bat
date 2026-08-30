@echo off
title Camila Nails - Entorno de Desarrollo
color 0d

echo ===================================================
echo     INICIANDO PROYECTO CAMILA NAILS
echo ===================================================
echo.

echo [1/3] Iniciando el Backend (Base de datos)...
start "Backend (Servidor)" cmd /k "cd server && npm start"

echo [2/3] Iniciando el Frontend (React)...
start "Frontend (React)" cmd /k "npm run dev"

echo [3/3] Abriendo tu navegador...
timeout /t 3 /nobreak > nul
start http://localhost:5173

echo.
echo Todo listo! Puedes cerrar esta ventana negra.
exit
