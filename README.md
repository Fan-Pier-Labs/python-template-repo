# Python Template Repository

A production-ready template for building applications with Python 3 and FastAPI. This template includes everything you need for both development and production deployment.

## ✨ Features

- **🐍 Python 3.11** - Modern Python runtime
- **⚡ FastAPI** - High-performance web framework
- **🐳 Docker Support** - Production-ready Dockerfile
- **💻 DevContainer** - Complete development environment with VS Code/Cursor support
- **🔧 Development Tools** - Pre-configured with essential dev tools (git, curl, build tools, etc.)
- **🐚 Fish Shell** - Fish shell configured as default with proper environment setup
- **🔐 GitHub CLI Integration** - Automatic token loading via fish function wrapper
- **☁️ AWS CLI** - Architecture-aware AWS CLI installation
- **🧪 Testing** - Pytest configured with async support
- **✅ Type Hints** - Full type hint support

## 🚀 Quick Start

### Using as a Template

1. Click "Use this template" on GitHub to create a new repository
2. Clone your new repository
3. Open in VS Code/Cursor with DevContainers extension
4. The container will automatically set up your development environment

### Local Development (without DevContainer)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
make install-dev

# Run the application
make run

# Run tests
make test
```

## 🛠️ Development Setup

### DevContainer (Recommended)

This repository includes a fully configured DevContainer that sets up:

- **Base Image**: `python:3.11-slim` - Official Python runtime
- **Development Tools**: Git, curl, wget, build tools, Python, fish shell, vim, nano, and more
- **GitHub CLI**: With automatic token loading (see below)
- **AWS CLI**: Architecture-aware installation (amd64/arm64)
- **Fish Shell**: Configured as default shell with proper environment variables

#### First Time Setup

1. Open the repository in VS Code/Cursor
2. When prompted, click "Reopen in Container"
3. The setup script will automatically:
   - Install all development tools
   - Configure fish shell
   - Set up GitHub CLI (if token file exists)
   - Install development dependencies

#### GitHub CLI Authentication

To use GitHub CLI in the container:

1. **On your Mac**, get your GitHub token:
   ```bash
   gh auth token
   ```

2. **Create the token file**:
   ```bash
   echo "your_token_here" > ~/.config/gh/gh_token
   chmod 600 ~/.config/gh/gh_token
   ```

3. The token file is automatically mounted into the container, and the fish function wrapper will use it automatically.

4. **For Mac users with fish shell**, copy the wrapper function:
   ```bash
   mkdir -p ~/.config/fish/functions
   cp .devcontainer/gh.fish ~/.config/fish/functions/gh.fish
   ```

Now `gh` commands will automatically use your token in both Mac and container environments!

## 🐳 Production Deployment

### Docker Build

The included `Dockerfile` is optimized for production:

```bash
# Build the image
docker build -t python-app .

# Run the container
docker run -p 8080:8080 python-app
```

**Features:**
- Uses Python 3.11 slim image (minimal size)
- Installs only production dependencies
- Runs your application with `python main.py`
- Includes health check endpoint

### Deployment

The `deploy.yaml` is configured for AWS Faragate deployment. Update the configuration values and run:

```bash
make deploy
```

This uses the deploy package installed via pip from the git repository in `requirements.txt`.

## 📁 Project Structure

```
.
├── .devcontainer/          # DevContainer configuration
│   ├── devcontainer.json   # Container settings and mounts
│   └── setup-dev.sh        # Development environment setup script
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD workflow
├── main.py                 # Application entry point
├── test_main.py            # Test suite
├── requirements.txt        # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── pytest.ini             # Pytest configuration
├── Makefile                # Common commands (make install, make test, etc.)
├── scripts/
│   └── deploy.py           # Deploy script wrapper
├── Dockerfile              # Production Docker image
├── deploy.yaml             # Deployment configuration
└── README.md              # This file
```

## 🔧 Development Tools Included

The setup script automatically installs:

- **Core Tools**: git, curl, wget, gnupg, openssh-client
- **Build Tools**: build-essential, make, cmake, pkg-config
- **Development Libraries**: libssl-dev, zlib1g-dev, libbz2-dev, etc.
- **Languages**: Python 3.11, pip, venv
- **Shells**: bash, zsh, fish
- **Editors**: vim, nano
- **Utilities**: htop, strace, jq, rsync, unzip, zip

## 🎯 Usage Examples

### Available Make Commands

```bash
make help        # Show all available commands
make install     # Install production dependencies
make install-dev # Install development dependencies
make test        # Run tests
make test-cov    # Run tests with coverage
make run         # Run the application
make deploy      # Deploy using deploy.yaml
make clean       # Clean up generated files
```

### Running Tests

```bash
make test
```

### Running Tests with Coverage

```bash
make test-cov
```

### Running the Application

```bash
make run
```

The application will be available at `http://localhost:8080`

### API Endpoints

- `GET /` - Root endpoint returning a greeting
- `GET /health` - Health check endpoint for monitoring

## 🔐 Environment Variables

- `PORT` - Server port (default: 8080)
- `HOST` - Server host (default: 0.0.0.0)

The DevContainer automatically sets:
- `XDG_CONFIG_HOME=/root/.local/config` - For fish shell configuration
- `GH_TOKEN` - Automatically loaded from `~/.config/gh/gh_token` (if present)

## 📝 Notes

- **Fish Shell**: The default shell is fish. Universal variables are stored in `/root/.local/config/fish/` to work with the read-only mounted config directory.
- **GitHub CLI**: The fish function wrapper automatically loads tokens from the mounted file, making authentication seamless.
- **Health Check**: The `/health` endpoint is available for health checks and monitoring.
- **FastAPI**: The application uses FastAPI which provides automatic API documentation at `/docs` and `/redoc` when running.

## 🤝 Contributing

This is a template repository. Feel free to:
1. Use it as a starting point for your projects
2. Customize the setup scripts for your needs
3. Add your own development tools and configurations

## 📄 License

This template is provided as-is for use in your projects.

---

Built with [Python](https://www.python.org/) and [FastAPI](https://fastapi.tiangolo.com/).
