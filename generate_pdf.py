#!/usr/bin/env python3
"""Generate PDF from portfolio-print.html using Playwright"""

from playwright.sync_api import sync_playwright
import os

html_path = os.path.abspath('/Users/priscilla/.openclaw/workspace/portfolio/portfolio-print.html')
pdf_path = '/Users/priscilla/.openclaw/workspace/portfolio/portfolio.pdf'

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Load the HTML file
    page.goto(f'file://{html_path}')
    
    # Wait for QR code images to load
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(2000)  # Extra time for QR images
    
    # Generate PDF with A4 size
    page.pdf(
        path=pdf_path,
        format='A4',
        print_background=True,
        margin={
            'top': '0mm',
            'right': '0mm',
            'bottom': '0mm',
            'left': '0mm'
        }
    )
    
    browser.close()

print(f"PDF generated: {pdf_path}")
