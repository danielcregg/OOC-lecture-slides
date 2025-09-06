const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function generatePDF(htmlPath, outputPath) {
  console.log(`Starting PDF generation for: ${htmlPath}`);
  
  if (!fs.existsSync(htmlPath)) {
    throw new Error(`HTML file does not exist: ${htmlPath}`);
  }
  
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--no-sandbox', 
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-web-security',
      '--disable-features=VizDisplayCompositor'
    ],
    executablePath: '/usr/bin/google-chrome-stable'
  });
  
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  
  const fullPath = 'file://' + path.resolve(htmlPath);
  console.log(`Loading: ${fullPath}`);
  
  await page.goto(fullPath, { 
    waitUntil: 'networkidle0',
    timeout: 30000 
  });
  
  console.log('Page loaded, adding print styles...');
  
  // Add reveal.js print CSS
  await page.addStyleTag({
    content: `
      @media print {
        .reveal .slides {
          width: 297mm !important;
          height: 210mm !important;
          left: 0 !important;
          top: 0 !important;
          transform: none !important;
          zoom: 1 !important;
        }
        .reveal .slides section {
          width: 297mm !important;
          height: 210mm !important;
          page-break-after: always !important;
          position: relative !important;
          margin: 0 !important;
          padding: 40px !important;
          box-sizing: border-box !important;
          display: flex !important;
          flex-direction: column !important;
          justify-content: center !important;
        }
        .reveal .backgrounds {
          display: none !important;
        }
        .reveal .progress {
          display: none !important;
        }
        .reveal .controls {
          display: none !important;
        }
      }
    `
  });
  
  // Wait for styles to apply
  await new Promise(resolve => setTimeout(resolve, 3000));
  
  console.log('Generating PDF...');
  
  const pdf = await page.pdf({
    path: outputPath,
    format: 'A4',
    landscape: true,
    printBackground: true,
    preferCSSPageSize: true,
    margin: {
      top: '10mm',
      right: '10mm',
      bottom: '10mm',
      left: '10mm'
    }
  });
  
  await browser.close();
  console.log(`PDF generated successfully: ${outputPath}`);
  return true;
}

async function main() {
  try {
    console.log('Starting PDF generation process...');
    
    // Create PDFs directory
    if (!fs.existsSync('pdfs')) {
      fs.mkdirSync('pdfs', { recursive: true });
      console.log('Created pdfs directory');
    }
    
    // Find all lecture HTML files
    const lecturesDir = 'lectures';
    if (!fs.existsSync(lecturesDir)) {
      throw new Error(`Lectures directory does not exist: ${lecturesDir}`);
    }
    
    const lectures = fs.readdirSync(lecturesDir, { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name)
      .sort();
    
    console.log(`Found lectures: ${lectures.join(', ')}`);
    
    let generatedCount = 0;
    for (const lecture of lectures) {
      const htmlPath = path.join(lecturesDir, lecture, 'index.html');
      if (fs.existsSync(htmlPath)) {
        const pdfPath = path.join('pdfs', `${lecture}.pdf`);
        await generatePDF(htmlPath, pdfPath);
        generatedCount++;
      } else {
        console.log(`Skipping ${lecture}: index.html not found`);
      }
    }
    
    console.log(`Successfully generated ${generatedCount} PDF files!`);
  } catch (error) {
    console.error('Error in main function:', error);
    process.exit(1);
  }
}

main();