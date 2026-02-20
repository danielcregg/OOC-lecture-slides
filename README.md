# OOC Lecture Slides

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

A comprehensive collection of interactive lecture slides for the Object-Oriented Computing (OOC) module, built with Reveal.js and hosted on GitHub Pages.

## Overview

This repository contains the full set of weekly lecture presentations for the OOC module at ATU. Each lecture is an interactive HTML slide deck covering Java programming fundamentals, object-oriented concepts, and AI-assisted programming techniques. The project also includes tooling for automated PDF generation and AI-narrated video creation of lectures.

## Features

- Interactive Reveal.js slide decks with keyboard navigation, speaker notes, and overview mode
- Responsive design that works on desktop, tablet, and mobile browsers
- Automated PDF export via GitHub Actions and Puppeteer
- AI-powered video generation with voice cloning for lecture narration
- Custom white theme with professional styling and animations
- GitHub Codespaces dev container for easy authoring
- Lecture template for consistent slide creation

## Prerequisites

- A modern web browser (Chrome 90+, Firefox 88+, Safari 14+, or Edge 90+)
- [Node.js](https://nodejs.org/) 18+ (for local development and PDF generation)
- [Python](https://www.python.org/) 3.10+ (for video generation scripts, optional)

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danielcregg/OOC-lecture-slides.git
   cd OOC-lecture-slides
   ```

2. Install Node.js dependencies (for PDF generation):
   ```bash
   npm install
   ```

### Usage

**View slides online:**
Visit the [GitHub Pages site](https://danielcregg.github.io/OOC-lecture-slides/) to browse all lectures.

**Serve locally:**

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx http-server
```

Then open `http://localhost:8000` in your browser.

**Slide navigation:**

| Key | Action |
|-----|--------|
| Arrow keys / Space | Navigate slides |
| `F` | Full-screen mode |
| `S` | Speaker notes |
| `Esc` | Overview mode |

## Tech Stack

- **Framework:** [Reveal.js](https://revealjs.com/) -- HTML presentation framework
- **Hosting:** GitHub Pages
- **PDF Generation:** Puppeteer via GitHub Actions
- **Video Generation:** Python with MiniMax TTS and voice cloning
- **Styling:** Custom CSS with responsive design
- **Dev Environment:** GitHub Codespaces / VS Code Dev Containers

## License

This project is licensed under the [MIT License](LICENSE).
