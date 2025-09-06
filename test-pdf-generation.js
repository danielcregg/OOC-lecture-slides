const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function generatePDF(htmlPath, outputPath) {
  console.log(`Starting PDF generation for: ${htmlPath}`);
  
  // Check if file exists
  if (!fs.existsSync(htmlPath)) {
    throw new Error(`HTML file does not exist: ${htmlPath}`);
  }
  
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    executablePath: '/usr/bin/google-chrome-stable'  // Use system Chrome
  });
  
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  
  const fullPath = 'file://' + path.resolve(htmlPath);
  console.log(`Loading: ${fullPath}`);
  
  await page.goto(fullPath, { 
    waitUntil: 'networkidle0',
    timeout: 30000 
  });
  
  console.log('Page loaded, generating PDF...');
  
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
}

async function main() {
  try {
    // Create PDFs directory
    if (!fs.existsSync('pdfs')) {
      fs.mkdirSync('pdfs', { recursive: true });
    }
    
    // Test with lecture-01
    const htmlPath = 'lectures/lecture-01/index.html';
    const pdfPath = 'pdfs/lecture-01.pdf';
    
    await generatePDF(htmlPath, pdfPath);
    
    console.log('PDF generation test completed successfully!');
  } catch (error) {
    console.error('Error during PDF generation:', error);
    process.exit(1);
  }
}

main();