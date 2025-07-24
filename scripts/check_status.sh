#!/bin/bash

SERVICE_NAME="daily-briefing"

echo "📊 Service Status:"
sudo systemctl status "$SERVICE_NAME.timer" --no-pager

echo -e "\n📅 Timer Schedule:"
sudo systemctl list-timers "$SERVICE_NAME.timer" --no-pager

echo -e "\n�� Recent Logs:"
sudo journalctl -u "$SERVICE_NAME.service" --since "1 hour ago" --no-pager