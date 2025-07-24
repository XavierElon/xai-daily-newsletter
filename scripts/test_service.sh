#!/bin/bash

SERVICE_NAME="daily-briefing"

echo "🧪 Testing service..."
sudo systemctl start "$SERVICE_NAME.service"

echo "�� Recent logs:"
sudo journalctl -u "$SERVICE_NAME.service" --since "1 minute ago" --no-pager

echo "📁 Checking for generated files:"
ls -la briefings/ 2>/dev/null || echo "No briefings directory found"