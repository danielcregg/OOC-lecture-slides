# AI-Assisted Programming - Lecture Slides

A comprehensive collection of interactive lecture slides for the AI-Assisted Programming course, built with Reveal.js and hosted on GitHub Pages.

## 🚀 View Slides Online

**Main Course Index**: [https://danielcregg.github.io/AIAP-lecture-slides/](https://danielcregg.github.io/AIAP-lecture-slides/)

## 📚 Course Structure

This course consists of 8 lectures, each approximately 60 minutes long:

1. **[Introduction to AI-Assisted Programming](lectures/lecture-01/)** ✅ Available
2. **Code Generation and Completion** 🚧 Coming Soon
3. **Code Review and Quality Assurance** 🚧 Coming Soon
4. **Testing and Debugging with AI** 🚧 Coming Soon
5. **Documentation and Communication** 🚧 Coming Soon
6. **AI in Software Architecture** 🚧 Coming Soon
7. **Ethics and Limitations** 🚧 Coming Soon
8. **Future of AI-Assisted Programming** 🚧 Coming Soon

## 🛠 Technology Stack

- **Framework**: [Reveal.js](https://revealjs.com/) - Modern HTML presentation framework
- **Hosting**: GitHub Pages
- **Styling**: Custom CSS with responsive design
- **Features**: 
  - Interactive navigation
  - Syntax highlighting for code examples
  - Responsive design for different screen sizes
  - Speaker notes support
  - Progress indicators

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
├── index.html              # Main course index page
├── lectures/               # Individual lecture folders
│   └── lecture-01/
│       └── index.html      # Lecture 1 slides
├── dist/                   # Reveal.js core files
├── plugin/                 # Reveal.js plugins
├── assets/                 # Shared images and resources
├── theme/                  # Custom theme files
├── _config.yml             # GitHub Pages configuration
└── README.md               # This file
```

## 🎯 Learning Objectives

By the end of this course, students will be able to:

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

1. **Create lecture folder**:
   ```bash
   mkdir lectures/lecture-XX
   ```

2. **Copy template**: Use `lectures/lecture-01/index.html` as a template

3. **Update main index**: Add the new lecture to `index.html`

4. **Follow naming convention**: Use `lecture-XX` format for consistency

### Lecture Template Structure

Each lecture should include:
- Title slide with lecture number and topic
- Learning objectives
- Content sections with fragments for progressive reveal
- Code examples with syntax highlighting
- Interactive elements (statistics, comparisons, etc.)
- Q&A section
- Navigation back to course index

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

We welcome contributions to improve the course content:

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

- **Course Instructor**: [Your Name]
- **Email**: [your.email@institution.edu]
- **GitHub Issues**: Use this repository's issue tracker for questions and suggestions

## 🙏 Acknowledgments

- [Reveal.js](https://revealjs.com/) for the excellent presentation framework
- [GitHub Pages](https://pages.github.com/) for free hosting
- The AI development community for valuable insights and statistics
