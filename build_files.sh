#!/bin/bash
set -e

echo "➡️ Creando entorno para Vercel (api/index.py)..."

# 1. Crear la carpeta api si no existe
mkdir -p api

# 2. Crear el archivo index.py dinámicamente
# Usamos printf para evitar problemas de saltos de línea
printf "from academia.wsgi import application\napp = application" > api/index.py

echo "✅ Archivo api/index.py creado."

# 3. Instalar dependencias con uv
echo "➡️ Instalando dependencias..."
uv sync

# 4. Recolectar archivos estáticos
echo "➡️ Ejecutando collectstatic..."
uv run python manage.py collectstatic --noinput --clear

echo "🚀 Build finalizado con éxito"