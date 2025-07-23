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
└── venv/ # Virtual environment (not tracked in git)


## Best Practices

1. **Always activate the virtual environment** before working on the project
2. **Keep requirements.txt updated** when adding new dependencies
3. **Never commit the venv directory** to version control (already in .gitignore)
4. **Use the same Python version** across development environments

## Troubleshooting

### If you get permission errors:
```bash
chmod +x venv/bin/activate
```

### If you need to recreate the environment:
```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Alternative: Using virtualenv
If you prefer `virtualenv` (which offers more features):
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Set up your virtual environment
4. Make your changes
5. Submit a pull request

## License

[Add your license information here]