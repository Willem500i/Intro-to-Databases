#!/usr/bin/env python3
"""
Script to convert markdown files to PDF using markdown and weasyprint
"""
import re
import subprocess
import sys

def markdown_to_html(md_content):
    """Simple markdown to HTML converter"""
    html = md_content
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # Code blocks
    html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Paragraphs (lines not starting with #, <, or empty)
    lines = html.split('\n')
    result = []
    in_para = False
    for line in lines:
        if line.strip() and not line.strip().startswith('<') and not line.strip().startswith('#'):
            if not in_para:
                result.append('<p>')
                in_para = True
            result.append(line)
        else:
            if in_para:
                result.append('</p>')
                in_para = False
            result.append(line)
    if in_para:
        result.append('</p>')
    html = '\n'.join(result)
    
    return html

def create_pdf_html(md_file, output_html):
    """Create HTML file that can be printed to PDF"""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    html_content = markdown_to_html(md_content)
    
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{md_file.replace('.md', '')}</title>
    <style>
        @page {{
            size: letter;
            margin: 1in;
        }}
        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
            page-break-after: avoid;
        }}
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 25px;
            page-break-after: avoid;
        }}
        h3 {{
            color: #555;
            margin-top: 20px;
            page-break-after: avoid;
        }}
        h4 {{
            color: #666;
            margin-top: 15px;
        }}
        p {{
            margin: 10px 0;
            text-align: justify;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-left: 4px solid #3498db;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            page-break-inside: avoid;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        strong {{
            color: #2c3e50;
        }}
        @media print {{
            body {{
                margin: 0;
                padding: 0;
            }}
            h1, h2, h3 {{
                page-break-after: avoid;
            }}
            pre {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
    
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Created {output_html}")
    print(f"Open {output_html} in a browser and use Print > Save as PDF to create the PDF")

if __name__ == '__main__':
    create_pdf_html('file_listing.md', 'file_listing.html')
    create_pdf_html('use_cases_queries.md', 'use_cases_queries.html')
    print("\nTo convert HTML to PDF:")
    print("1. Open the HTML files in a browser")
    print("2. Use File > Print > Save as PDF")
    print("OR use: open file_listing.html && open use_cases_queries.html")

