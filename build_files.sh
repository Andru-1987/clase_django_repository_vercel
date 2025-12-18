#!/bin/bash

# Salir inmediatamente si un comando falla
set -e

echo "➡️ Instalando dependencias..."
# Vercel usa python3 por defecto
python3 -m pip install -r requirements.txt

echo "➡️ Ejecutando collectstatic..."
# Esto usa la configuración de STATIC_ROOT de tu settings.py
python3 manage.py collectstatic --noinput --clear

echo "✅ Build finalizado con éxito"