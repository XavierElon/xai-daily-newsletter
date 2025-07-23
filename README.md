
# XAI Daily Newsletter

A Python project for generating AI-powered daily newsletters.

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Virtual Environment Setup

1. **Navigate to the project directory**:
   ```bash
   cd /home/xxx/Documents/coding/xai-daily-newsletter
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```
   This creates a new directory called `venv` containing the virtual environment.

3. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```
   You'll know it's activated when you see `(venv)` at the beginning of your command prompt.

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Using the Virtual Environment

### Activating the Environment
```bash
source venv/bin/activate
```

### Installing New Packages
```bash
pip install package_name
```

### Updating Requirements
After installing new packages, update the requirements file:
```bash
pip freeze > requirements.txt
```

### Deactivating the Environment
```bash
deactivate
```

## Project Structure

xai-daily-newsletter/
├── README.md
├── requirements.txt
├── .gitignore
├── generate_daily_briefing.py
├── email_sender.py
├── scheduler.py
├── daily-briefing.service
├── briefings/
│ └── MM-YYYY/
│ └── briefing_tech_briefing_YYYY-MM-DD.txt
└── venv/ # Virtual environment (not tracked in git)


## Automated Daily Briefing

### Systemd Daemon Setup

This project uses **systemd** (a Linux daemon) to automatically generate and email daily briefings.

#### What is systemd?
- **systemd** is the system and service manager for Linux
- It runs as a **daemon** (background process) with PID 1
- It manages all system services and processes
- Your daily-briefing service runs as a **managed daemon** under systemd

#### Setting up the service:

1. **Install the systemd service**:
   ```bash
   sudo cp daily-briefing.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable daily-briefing.service
   sudo systemctl start daily-briefing.service
   ```

2. **Check service status**:
   ```bash
   sudo systemctl status daily-briefing.service
   ```

3. **View service logs**:
   ```bash
   sudo journalctl -u daily-briefing.service -f
   ```

#### Service Management Commands:
```bash
# Start the service
sudo systemctl start daily-briefing.service

# Stop the service
sudo systemctl stop daily-briefing.service

# Restart the service
sudo systemctl restart daily-briefing.service

# Check if enabled (starts on boot)
sudo systemctl is-enabled daily-briefing.service

# Disable the service
sudo systemctl disable daily-briefing.service
```

#### How it works:
1. **systemd daemon** runs continuously in the background
2. Your `daily-briefing.service` is registered with systemd
3. systemd starts your service and monitors it
4. Your service runs as a **managed daemon** under systemd supervision
5. All output is logged to systemd's journal

## Environment Variables

Create a `.env` file in the project root:
```env
# XAI API
XAI_API_KEY=your_xai_api_key

# Email Configuration
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## Best Practices

1. **Always activate the virtual environment** before working on the project
2. **Keep requirements.txt updated** when adding new dependencies
3. **Never commit the venv directory** to version control (already in .gitignore)
4. **Use the same Python version** across development environments
5. **Never commit `.env` files** to version control
6. **Use app passwords** for Gmail, not your main password

## Troubleshooting

### Virtual Environment Issues

#### If you get permission errors:
```bash
chmod +x venv/bin/activate
```

#### If you need to recreate the environment:
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Alternative: Using virtualenv
If you prefer `virtualenv` (which offers more features):
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### Systemd Service Issues

#### Check if systemd daemon is running:
```bash
sudo systemctl status
```

#### Check your service status:
```bash
sudo systemctl status daily-briefing.service
```

#### View service logs:
```bash
sudo journalctl -u daily-briefing.service -f
```

#### Test the service manually:
```bash
sudo systemctl start daily-briefing.service
sudo journalctl -u daily-briefing.service --since "1 minute ago"
```

#### Check if files were created:
```bash
ls -la briefings/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Set up your virtual environment
4. Make your changes
5. Submit a pull request

## License

[Add your license information here]