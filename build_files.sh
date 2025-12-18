#!/bin/bash
set -e

echo "➡️ Instalando dependencias con uv..."
uv sync

echo "➡️ Ejecutando collectstatic (ignorando venv)..."
# Añadimos --ignore para que no meta la basura del entorno virtual en tus estáticos
uv run python manage.py collectstatic --noinput --clear --ignore venv --ignore .venv

echo "🚀 Build finalizado"