#!/bin/bash
set -e

echo "➡️ Iniciando Build con uv..."

# 1. Instalar dependencias usando el lockfile (Vercel ya lo hace, pero esto asegura consistencia)
uv sync

# 2. Ejecutar collectstatic de Django
# Usamos 'uv run' para asegurarnos de usar el venv correcto
echo "➡️ Ejecutando collectstatic..."
uv run python manage.py collectstatic --noinput --clear

echo "✅ Build finalizado con éxito"