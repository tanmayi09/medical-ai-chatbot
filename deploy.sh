#!/bin/bash

set -Eeuo pipefail

APP_DIR="/var/www/medical-ai-chatbot"
SERVICE_NAME="medical-ai-chatbot"

echo "Starting deployment..."

cd "$APP_DIR"

echo "Pulling latest code..."
git pull --ff-only origin main

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running tests..."
pytest

echo "Restarting application..."
sudo systemctl restart "$SERVICE_NAME"

echo "Checking application status..."
sudo systemctl is-active --quiet "$SERVICE_NAME"

echo "Checking health endpoint..."
curl --fail --silent --show-error http://127.0.0.1:8000/health

echo ""
echo "Deployment successful!"