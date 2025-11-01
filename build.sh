#!/bin/bash
set -e

echo "===================="
echo "STARTING BUILD PROCESS"
echo "===================="

echo "Step 1: Installing Python dependencies"
uv install --python=python3

echo "Step 2: Installing Node.js dependencies"
npm install

echo "Step 3: Building static files (npm run build)"
npm run build

echo "Step 4: Collecting static files"
python3 manage.py collectstatic --noinput --clear

echo "Step 5: Applying database migrations"
python3 manage.py migrate

echo "===================="
echo "✅ BUILD PROCESS COMPLETED SUCCESSFULLY"
echo "===================="
