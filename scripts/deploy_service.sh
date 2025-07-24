#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
SERVICE_NAME="daily-briefing"
PROJECT_DIR="/home/xxx/Documents/coding/xai-daily-newsletter"
SERVICE_FILE="$PROJECT_DIR/daily-briefing.service"
TIMER_FILE="$PROJECT_DIR/daily-briefing.timer"

echo -e "${YELLOW}🚀 Deploying Daily Briefing Service...${NC}"

# Check if files exist
if [ ! -f "$SERVICE_FILE" ]; then
    echo -e "${RED}❌ Service file not found: $SERVICE_FILE${NC}"
    exit 1
fi

if [ ! -f "$TIMER_FILE" ]; then
    echo -e "${RED}❌ Timer file not found: $TIMER_FILE${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Service files found${NC}"

# Copy files to systemd directory
echo -e "${YELLOW}📋 Copying service files to systemd...${NC}"
sudo cp "$SERVICE_FILE" /etc/systemd/system/
sudo cp "$TIMER_FILE" /etc/systemd/system/

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Files copied successfully${NC}"
else
    echo -e "${RED}❌ Failed to copy files${NC}"
    exit 1
fi

# Reload systemd daemon
echo -e "${YELLOW}🔄 Reloading systemd daemon...${NC}"
sudo systemctl daemon-reload

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Systemd daemon reloaded${NC}"
else
    echo -e "${RED}❌ Failed to reload systemd${NC}"
    exit 1
fi

# Stop and disable old service (if it exists)
echo -e "${YELLOW}🛑 Stopping old service...${NC}"
sudo systemctl stop "$SERVICE_NAME.service" 2>/dev/null
sudo systemctl disable "$SERVICE_NAME.service" 2>/dev/null

# Enable and start the timer
echo -e "${YELLOW}⏰ Enabling timer...${NC}"
sudo systemctl enable "$SERVICE_NAME.timer"
sudo systemctl start "$SERVICE_NAME.timer"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Timer started successfully${NC}"
else
    echo -e "${RED}❌ Failed to start timer${NC}"
    exit 1
fi

# Show status
echo -e "${YELLOW}📊 Service Status:${NC}"
sudo systemctl status "$SERVICE_NAME.timer" --no-pager

echo -e "${YELLOW}📅 Timer Schedule:${NC}"
sudo systemctl list-timers "$SERVICE_NAME.timer" --no-pager

echo -e "${GREEN}🎉 Deployment complete!${NC}"
echo -e "${YELLOW}�� Useful commands:${NC}"
echo -e "  Check status: sudo systemctl status $SERVICE_NAME.timer"
echo -e "  View logs: sudo journalctl -u $SERVICE_NAME.service -f"
echo -e "  Test manually: sudo systemctl start $SERVICE_NAME.service"
echo -e "  Stop service: sudo systemctl stop $SERVICE_NAME.timer"