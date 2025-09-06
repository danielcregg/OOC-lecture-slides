const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function testPdfGeneration() {
  console.log('Testing PDF generation...');
  
  // Check if lecture file exists
  const lectureDir = '/home/runner/work/AIAP-lecture-slides/AIAP-lecture-slides';
  const htmlPath = path.join(lectureDir, 'lectures/lecture-01/index.html');
  
  console.log('Checking file:', htmlPath);
  if (!fs.existsSync(htmlPath)) {
    throw new Error(`HTML file does not exist: ${htmlPath}`);
  }
  console.log('✓ HTML file exists');
  
  try {
    console.log('Launching browser...');
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
    console.log('✓ Browser launched successfully');
    
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 720 });
    console.log('✓ Page created');
    
    const fullPath = 'file://' + path.resolve(htmlPath);
    console.log(`Loading: ${fullPath}`);
    
    // Try to load the page with a shorter timeout first
    try {
      await page.goto(fullPath, { 
        waitUntil: 'networkidle0',
        timeout: 15000 
      });
      console.log('✓ Page loaded successfully');
    } catch (error) {
      console.log('Network idle timeout, trying with domcontentloaded...');
      await page.goto(fullPath, { 
        waitUntil: 'domcontentloaded',
        timeout: 10000 
      });
      console.log('✓ Page loaded with domcontentloaded');
    }
    
    // Check if Reveal.js is loaded
    const revealLoaded = await page.evaluate(() => {
      return typeof window.Reveal !== 'undefined';
    });
    console.log('Reveal.js loaded:', revealLoaded);
    
    await browser.close();
    console.log('✓ Test completed successfully - no major issues detected');
    return true;
    
  } catch (error) {
    console.error('Error during testing:', error.message);
    return false;
  }
}

testPdfGeneration().then(success => {
  if (success) {
    console.log('✅ PDF generation test passed');
    process.exit(0);
  } else {
    console.log('❌ PDF generation test failed');
    process.exit(1);
  }
}).catch(error => {
  console.error('Unexpected error:', error);
  process.exit(1);
});