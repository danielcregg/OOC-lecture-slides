#!/usr/bin/env python3
"""
Update front page index.html with available PDF and video links.
This script scans for available PDFs and videos, then updates the index.html 
to include proper hosted GitHub Pages links for each lecture.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class FrontPageUpdater:
    def __init__(self):
        self.github_pages_base = "https://danielcregg.github.io/AIAP-lecture-slides"
        self.index_file = Path("index.html")
        self.pdfs_dir = Path("pdfs")
        self.videos_dir = Path("videos")
        self.lectures_dir = Path("lectures")
        
    def scan_available_content(self) -> Dict[str, Dict]:
        """Scan for available PDFs, videos, and HTML slides."""
        content = {}
        
        # Scan PDFs
        if self.pdfs_dir.exists():
            for pdf_file in self.pdfs_dir.glob("*.pdf"):
                lecture_name = pdf_file.stem
                if lecture_name not in content:
                    content[lecture_name] = {}
                content[lecture_name]['pdf'] = f"{self.github_pages_base}/pdfs/{pdf_file.name}"
                
        # Scan Videos
        if self.videos_dir.exists():
            for video_file in self.videos_dir.glob("*.mp4"):
                lecture_name = video_file.stem
                if lecture_name not in content:
                    content[lecture_name] = {}
                content[lecture_name]['video'] = f"{self.github_pages_base}/videos/{video_file.name}"
                
        # Scan HTML lectures
        if self.lectures_dir.exists():
            for html_file in self.lectures_dir.glob("*.html"):
                lecture_name = html_file.stem
                if lecture_name not in content:
                    content[lecture_name] = {}
                content[lecture_name]['slides'] = f"lectures/{html_file.name}"
                
        return content
        
    def extract_lecture_info(self, lecture_name: str) -> Tuple[Optional[int], str]:
        """Extract lecture number and title from filename."""
        # Handle format: lecture1-module-introduction -> (1, "Module Introduction")
        match = re.match(r'lecture(\d+)-(.+)', lecture_name)
        if match:
            number = int(match.group(1))
            title = match.group(2).replace('-', ' ')
            # Properly capitalize title with special handling for AI
            words = title.split()
            capitalized_words = []
            for word in words:
                if word.lower() == 'ai':
                    capitalized_words.append('AI')
                else:
                    capitalized_words.append(word.capitalize())
            title = ' '.join(capitalized_words)
            return number, title
        return None, lecture_name
        
    def get_lecture_description(self, lecture_name: str) -> str:
        """Get appropriate description for each lecture."""
        descriptions = {
            'lecture1-module-introduction': 'Welcome to AIAP! Module overview, learning outcomes, assessment details, and getting started with tools.',
            'lecture2-structure': 'Hello World, program structure, compile/run, variables, control flow, methods, arrays, objects.',
            'lecture3-code-generation-completion': 'Deep dive into AI-powered code generation, best practices, and hands-on exercises with various AI tools.',
            'lecture4-debugging-testing': 'AI-powered debugging techniques, automated testing with AI, and quality assurance strategies.',
            'lecture5-documentation-comments': 'Generating documentation with AI, code commenting best practices, and maintaining code clarity.',
            'lecture6-code-review-refactoring': 'AI-assisted code reviews, automated refactoring techniques, and improving code quality.',
            'lecture7-project-management': 'Using AI for project planning, task automation, and development workflow optimization.',
            'lecture8-ethics-best-practices': 'Ethical considerations in AI-assisted programming, security implications, and industry best practices.',
        }
        return descriptions.get(lecture_name, 'Comprehensive coverage of AI-assisted programming concepts and practical applications.')
        
    def get_lecture_duration(self, lecture_name: str) -> str:
        """Get duration for each lecture."""
        durations = {
            'lecture1-module-introduction': '45 minutes',
            'lecture2-structure': '60 minutes',
            'lecture3-code-generation-completion': '60 minutes',
            'lecture4-debugging-testing': '55 minutes',
            'lecture5-documentation-comments': '50 minutes',
            'lecture6-code-review-refactoring': '65 minutes',
            'lecture7-project-management': '55 minutes',
            'lecture8-ethics-best-practices': '60 minutes',
        }
        return durations.get(lecture_name, '60 minutes')
        
    def generate_lecture_card(self, lecture_name: str, content: Dict, available: bool = True) -> str:
        """Generate HTML for a lecture card."""
        number, title = self.extract_lecture_info(lecture_name)
        description = self.get_lecture_description(lecture_name)
        duration = self.get_lecture_duration(lecture_name)
        
        if not available:
            duration += " - Coming Soon"
            
        week_text = f"Week {number}" if number else "TBD"
        
        # Build the card HTML
        card_class = "lecture-card available" if available else "lecture-card coming-soon"
        onclick_attr = f'onclick="window.location.href=\'{content.get("slides", "#")}\'"' if available and content.get("slides") else ""
        
        card_html = f'''        <div class="{card_class}" {onclick_attr}>
            <div class="lecture-number">{week_text}</div>
            <div class="lecture-title">{title}</div>
            <div class="lecture-description">
                {description}
            </div>
            <div class="lecture-duration">{duration}</div>'''
            
        # Add resources section
        if available and (content.get('pdf') or content.get('video')):
            card_html += '''
            <div class="lecture-resources">'''
            
            if content.get('pdf'):
                card_html += f'''
                <a href="{content['pdf']}" class="resource-link pdf-resource" onclick="event.stopPropagation();" target="_blank">
                    📄 PDF
                </a>'''
                
            if content.get('video'):
                card_html += f'''
                <a href="{content['video']}" class="resource-link video-resource" onclick="event.stopPropagation();" target="_blank">
                    🎥 Video
                </a>'''
                
            card_html += '''
            </div>'''
        elif not available:
            # Add placeholder resources for coming soon
            card_html += '''
            <div class="lecture-resources">
                <span class="resource-link pdf-resource">📄 PDF</span>
                <span class="resource-link video-resource">🎥 Video</span>
            </div>'''
            
        card_html += '''
        </div>'''
        
        return card_html
        
    def update_index_html(self, content: Dict[str, Dict]) -> bool:
        """Update the index.html file with new lecture cards."""
        if not self.index_file.exists():
            print(f"Error: {self.index_file} not found")
            return False
            
        print(f"Reading {self.index_file}")
        with open(self.index_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Find the lectures grid section
        grid_start_pattern = r'<div class="lecture-grid">'
        grid_end_pattern = r'</div>\s*<div class="pdf-link">'
        
        grid_start_match = re.search(grid_start_pattern, html_content)
        grid_end_match = re.search(grid_end_pattern, html_content)
        
        if not grid_start_match or not grid_end_match:
            print("Error: Could not find lectures grid section in index.html")
            return False
            
        # Extract sections
        before_grid = html_content[:grid_start_match.end()]
        after_grid = html_content[grid_end_match.start():]
        
        # Generate new lecture cards
        print("Generating lecture cards...")
        cards_html = []
        
        # Sort available content by lecture number
        sorted_lectures = sorted(
            [(name, info) for name, info in content.items() if self.extract_lecture_info(name)[0] is not None],
            key=lambda x: self.extract_lecture_info(x[0])[0]
        )
        
        # Add available lectures
        for lecture_name, lecture_content in sorted_lectures:
            has_content = bool(lecture_content.get('pdf') or lecture_content.get('video') or lecture_content.get('slides'))
            card_html = self.generate_lecture_card(lecture_name, lecture_content, available=has_content)
            cards_html.append(card_html)
            number, title = self.extract_lecture_info(lecture_name)
            print(f"  ✅ Week {number}: {title} {'(with resources)' if has_content else '(slides only)'}")
            
        # Add placeholder cards for upcoming lectures if we have fewer than 8
        max_lectures = 8
        current_count = len(sorted_lectures)
        
        for i in range(current_count + 1, max_lectures + 1):
            placeholder_name = f"lecture{i}-placeholder"
            placeholder_content = {}
            card_html = self.generate_lecture_card(placeholder_name, placeholder_content, available=False)
            cards_html.append(card_html)
            
        # Build the complete grid content
        grid_content = f'''
{chr(10).join(cards_html)}
        '''
        
        # Reconstruct the HTML
        new_html = before_grid + grid_content + after_grid
        
        # Write the updated file
        print(f"Writing updated {self.index_file}")
        with open(self.index_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
            
        return True
        
    def run(self) -> bool:
        """Run the front page update process."""
        print("🔄 Updating front page with available content...")
        
        # Scan for available content
        print("📁 Scanning for available content...")
        content = self.scan_available_content()
        
        if not content:
            print("⚠️  No content found to update front page with")
            return False
            
        print(f"Found content for {len(content)} lectures:")
        for name, info in sorted(content.items()):
            number, title = self.extract_lecture_info(name)
            resources = []
            if info.get('pdf'):
                resources.append('PDF')
            if info.get('video'):
                resources.append('Video')
            if info.get('slides'):
                resources.append('Slides')
            resource_text = f" ({', '.join(resources)})" if resources else ""
            print(f"  📚 {name}: {title}{resource_text}")
            
        # Update index.html
        success = self.update_index_html(content)
        
        if success:
            print("✅ Front page updated successfully!")
        else:
            print("❌ Failed to update front page")
            
        return success

def main():
    updater = FrontPageUpdater()
    success = updater.run()
    
    if not success:
        print("❌ Front page update failed")
        exit(1)
    else:
        print("✅ Front page update completed")

if __name__ == "__main__":
    main()