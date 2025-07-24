#!/bin/bash

SERVICE_NAME="daily-briefing"

echo "🛑 Stopping daily briefing service..."
sudo systemctl stop "$SERVICE_NAME.timer"
sudo systemctl disable "$SERVICE_NAME.timer"

echo "✅ Service stopped and disabled"