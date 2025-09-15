# AI-Assisted Programming - Lecture Slides

A comprehensive collection of interactive lecture slides for the AI-Assisted Programming module, built with Reveal.js and hosted on GitHub Pages.

## 🚀 View Slides Online

**Main Module Index**: [https://danielcregg.github.io/AIAP-lecture-slides/](https://danielcregg.github.io/AIAP-lecture-slides/)

## 📚 Module Structure

This module consists of a module introduction plus 8 main lectures:

1. **[Module Introduction](https://danielcregg.github.io/AIAP-lecture-slides/lectures/lecture1-module-introduction.html)** ✅ Available | [📄 PDF](https://github.com/danielcregg/AIAP-lecture-slides/raw/main/pdfs/lecture1-module-introduction.pdf)
2. **[Ai Assisted Programming Intro](https://danielcregg.github.io/AIAP-lecture-slides/lectures/lecture2-ai-assisted-programming-intro.html)** ✅ Available | [📄 PDF](https://github.com/danielcregg/AIAP-lecture-slides/raw/main/pdfs/lecture2-ai-assisted-programming-intro.pdf) | [🎥 Video](https://danielcregg.github.io/AIAP-lecture-slides/videos/lecture2-ai-assisted-programming-intro.mp4)
3. **Testing and Debugging with AI** 🚧 Coming Soon
4. **Documentation and Communication** 🚧 Coming Soon
5. **AI in Software Architecture** 🚧 Coming Soon
6. **Ethics and Limitations** 🚧 Coming Soon
7. **Future of AI-Assisted Programming** 🚧 Coming Soon
8. **Lecture 8** 🚧 Coming Soon
9. **Lecture 9** 🚧 Coming Soon


## 📄 PDF Downloads

All lectures are available as PDF downloads for offline viewing and printing:

- **[Download All PDFs](pdfs/)** - Browse the complete PDF directory
- **Individual PDFs** - Click the 📄 PDF links next to each lecture above
- **Auto-Generated** - PDFs are automatically updated when slides change

## 🛠 Technology Stack

- **Framework**: [Reveal.js](https://revealjs.com/) - Modern HTML presentation framework
- **Hosting**: GitHub Pages
- **Styling**: Custom CSS with responsive design
- **PDF Generation**: Automated via GitHub Actions with Puppeteer
- **Features**: 
  - Interactive navigation
  - Syntax highlighting for code examples
  - Responsive design for different screen sizes
  - Speaker notes support
  - Progress indicators
  - Automated PDF export

## 📖 Features

### Interactive Presentations
- **Keyboard Navigation**: Use arrow keys, spacebar, or touch gestures
- **Full-Screen Mode**: Press `F` for full-screen presentation
- **Speaker Notes**: Press `S` to open speaker notes window
- **Overview Mode**: Press `Esc` to see all slides at once

### Content Features
- **Up-to-date Statistics**: All data reflects 2024 market research
- **Code Examples**: Syntax-highlighted code with live editing capability
- **Interactive Elements**: Animated reveals and transitions
- **Visual Data**: Charts, graphs, and statistical visualizations
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## 🏗 Repository Structure

```
AIAP-lecture-slides/
├── index.html                                    # Main module index page
├── lectures/                                     # Individual lecture files
│   ├── lecture1-module-introduction.html        # Module introduction
│   └── lecture2-ai-assisted-programming-intro.html # Lecture 2 slides
├── pdfs/                                         # Auto-generated PDF exports
│   ├── lecture1-module-introduction.pdf
│   └── lecture2-ai-assisted-programming-intro.pdf
├── dist/                                         # Reveal.js core files
├── plugin/                                       # Reveal.js plugins
├── theme/                                        # Custom theme files
├── .github/workflows/                            # GitHub Actions for PDF generation
├── _config.yml                                   # GitHub Pages configuration
└── README.md                                     # This file
```

## 🎯 Learning Objectives

By the end of this module, students will be able to:

- Understand the landscape of AI-assisted programming tools
- Effectively use GitHub Copilot and similar AI coding assistants
- Apply best practices for AI-assisted development
- Evaluate code quality and security in AI-generated code
- Navigate ethical considerations in AI-assisted programming
- Prepare for the evolving future of software development

## 💻 Local Development

To run these slides locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/danielcregg/AIAP-lecture-slides.git
   cd AIAP-lecture-slides
   ```

2. **Serve locally** (choose one method):
   
   **Using Python:**
   ```bash
   python -m http.server 8000
   ```
   
   **Using Node.js:**
   ```bash
   npx http-server
   ```
   
   **Using PHP:**
   ```bash
   php -S localhost:8000
   ```

3. **Open in browser**: Navigate to `http://localhost:8000`

## 📝 Adding New Lectures

To add a new lecture:

1. **Create lecture file**:
   ```bash
   # Follow the naming convention: lecture#-descriptive-title.html
   cp lectures/lecture2-ai-assisted-programming-intro.html lectures/lecture3-new-topic.html
   ```

2. **Update content**: Edit the new HTML file with your content

3. **Update main index**: Add the new lecture to `index.html`

4. **Follow naming convention**: Use `lecture-##-descriptive-title.html` format

5. **PDF Generation**: PDFs will be automatically generated by GitHub Actions

### Lecture File Naming

- **Format**: `lecture#-descriptive-title.html`
- **Examples**: 
  - `lecture1-module-introduction.html`
  - `lecture2-ai-assisted-programming-intro.html`
  - `lecture3-code-generation-basics.html`

### Lecture Template Structure

Each lecture should include:
- Title slide with lecture number and topic
- Learning objectives
- Content sections with fragments for progressive reveal
- Code examples with syntax highlighting
- Interactive elements (statistics, comparisons, etc.)
- Q&A section
- Navigation back to module index

## 🎨 Customization

### Themes
- Current theme: Modified "Black" theme with custom blue accents (#42affa)
- Theme files located in `dist/theme/`
- Custom styles in each lecture's `<style>` section

### Colors
- Primary: #42affa (Blue)
- Success: #4CAF50 (Green)
- Warning: #f44336 (Red)
- Background: #191919 (Dark gray)

## 📊 Content Sources

All statistics and information are sourced from:
- Stack Overflow Developer Survey 2024
- GitHub Research Studies
- Industry reports from major tech companies
- Academic research papers
- Official documentation from AI tool providers

## 🤝 Contributing

We welcome contributions to improve the module content:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-lecture`
3. **Make your changes**
4. **Test locally** to ensure slides work properly
5. **Submit a pull request**

### Contribution Guidelines
- Ensure all statistics are current and properly sourced
- Follow the existing slide structure and styling
- Test on multiple screen sizes
- Include speaker notes for complex topics
- Maintain consistent formatting and terminology

## 📱 Browser Support

Tested and supported on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

- **Module Instructor**: [Your Name]
- **Email**: [your.email@institution.edu]
- **GitHub Issues**: Use this repository's issue tracker for questions and suggestions

## 🙏 Acknowledgments

- [Reveal.js](https://revealjs.com/) for the excellent presentation framework
- [GitHub Pages](https://pages.github.com/) for free hosting
- The AI development community for valuable insights and statistics
