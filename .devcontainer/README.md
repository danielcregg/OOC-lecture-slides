# Dev Container for AIAP Lecture Slides

This directory contains the development container configuration for the AI-Assisted Programming lecture slides project. This setup ensures a consistent development environment across all contributors using GitHub Codespaces or VS Code with the Dev Containers extension.

## 🚀 Quick Start

### Using GitHub Codespaces
1. Click the **Code** button on the GitHub repository
2. Select **Codespaces** tab
3. Click **Create codespace on main**
4. Wait for the container to build and start

### Using VS Code Dev Containers
1. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open the repository in VS Code
3. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
4. Run "Dev Containers: Reopen in Container"

## 📦 What's Included

### Pre-installed Extensions
- **GitHub Codespaces** - Core codespace functionality
- **GitHub Copilot** - AI-powered code completion
- **GitHub Copilot Chat** - AI-powered chat assistance  
- **GitHub Theme** - Official GitHub theme
- **GitHub Actions** - Workflow editing support
- **GitHub Pull Requests** - PR management
- **Gemini Code Assist** - Google's AI code assistant
- **PDF Viewer** - View PDFs directly in VS Code
- **Live Server** - Local development server
- **Copilot Vision** - Visual code assistance
- **Web Search for Copilot** - Enhanced search capabilities

### Development Tools
- **Node.js 18** - JavaScript runtime for build tools
- **Git** - Version control (latest version)
- **GitHub CLI** - Command-line GitHub integration
- **http-server** - Simple HTTP server for serving static files

### Port Configuration
The following ports are automatically forwarded:
- **5500** - Live Server (auto-opens in browser)
- **8000** - Python HTTP Server
- **3000** - Development Server  
- **4000** - Static Site Server

## ⚙️ Environment Features

### VS Code Settings
- **Theme**: GitHub Dark
- **Font Size**: 14px
- **Tab Size**: 2 spaces
- **Auto Save**: Enabled (1 second delay)
- **Word Wrap**: Enabled
- **Bracket Pair Colorization**: Enabled
- **Minimap**: Enabled

### HTML/CSS Settings
- **HTML Indentation**: Inner HTML indented
- **Line Wrap**: 120 characters
- **CSS Spacing**: Proper spacing around selectors

### Live Server Configuration
- **Default Port**: 5500
- **Auto-open**: Enabled
- **Info Messages**: Disabled for cleaner output

## 🛠 Development Workflow

### Serving Slides Locally
1. **Using Live Server Extension**:
   - Right-click on any HTML file
   - Select "Open with Live Server"
   - Browser opens automatically

2. **Using Command Line**:
   ```bash
   # Using http-server (pre-installed)
   http-server -p 5500
   
   # Using Python (if available)
   python -m http.server 8000
   
   # Using Node.js
   npx http-server -p 3000
   ```

### PDF Generation
PDFs are automatically generated via GitHub Actions, but you can also generate them locally:
```bash
# Install dependencies
npm install puppeteer

# Run the PDF generation script
node generate-pdfs.js
```

### Working with Git
```bash
# GitHub CLI is pre-installed
gh repo status
gh pr list
gh pr create

# Standard git commands work as expected
git status
git add .
git commit -m "Update slides"
git push
```

## 📁 Directory Structure

```
.devcontainer/
├── devcontainer.json    # Main configuration
└── README.md           # This file
```

## 🔧 Customization

### Adding Extensions
Edit `.devcontainer/devcontainer.json` and add extension IDs to the `extensions` array:
```json
"extensions": [
  "existing.extension",
  "new.extension-id"
]
```

### Modifying Settings
Update the `settings` object in `devcontainer.json`:
```json
"settings": {
  "editor.fontSize": 16,
  "workbench.colorTheme": "Dark+"
}
```

### Adding Features
Add new development tools in the `features` section:
```json
"features": {
  "ghcr.io/devcontainers/features/python:1": {
    "version": "3.11"
  }
}
```

## 🐛 Troubleshooting

### Container Won't Start
1. Check if Docker is running (for local dev containers)
2. Verify the `devcontainer.json` syntax is valid
3. Try rebuilding the container: "Dev Containers: Rebuild Container"

### Extensions Not Loading
1. Check the extension IDs are correct
2. Verify the extensions are compatible with the base image
3. Try reloading the window: "Developer: Reload Window"

### Port Forwarding Issues
1. Check if ports are already in use
2. Update port numbers in `devcontainer.json`
3. Manually forward ports in VS Code ports panel

## 📚 Resources

- [Dev Containers Documentation](https://containers.dev/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/remote/containers)
- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)
- [Reveal.js Documentation](https://revealjs.com/)

## 🤝 Contributing

When contributing to this project:
1. Use the dev container for consistent environment
2. Test your changes locally before pushing
3. Ensure slides work in both development and production
4. Follow the established coding and documentation standards

---

*This dev container configuration is optimized for the AIAP lecture slides project. For general web development, you may want to customize the settings and extensions.*