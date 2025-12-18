#!/bin/bash
set -e

echo "➡️ Build: preparando static files"

mkdir -p public/static

# Copia todos los static de las apps
cp -r entidades/static/* public/static/

echo "✅ Static files copiados a public/static"
ls -R public/static
