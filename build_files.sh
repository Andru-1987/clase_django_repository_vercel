#!/bin/bash
set -e

echo "➡️ Creando carpeta api/..."
mkdir -p api

# Crear el archivo index.py que conecta con Django
echo "from academia.wsgi import application" > api/index.py
echo "app = application" >> api/index.py

echo "➡️ Instalando dependencias con uv..."
uv sync

echo "➡️ Ejecutando collectstatic..."
# Usamos --no-input para que no pida confirmación en el servidor
uv run python manage.py collectstatic --noinput --clear

# Truco: creamos una carpeta public vacía solo para satisfacer a Vercel si fuera necesario
mkdir -p public

echo "🚀 Build finalizado con éxito"