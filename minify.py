import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Minify CSS
def minify_css(match):
    css = match.group(1)
    # Remove CSS comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Remove newlines and tabs
    css = re.sub(r'[\r\n\t]+', ' ', css)
    # Remove multiple spaces
    css = re.sub(r' +', ' ', css)
    # Remove spaces around {} ; : ,
    css = re.sub(r'\s*([\{\}\;\:\,])\s*', r'\1', css)
    return '<style>' + css + '</style>'

html = re.sub(r'<style>(.*?)</style>', minify_css, html, flags=re.DOTALL)

# Minify JS
def minify_js(match):
    js = match.group(1)
    # Basic minification for this specific script
    js = re.sub(r'//.*', '', js) # remove single line comments
    js = re.sub(r'[\r\n\t]+', ' ', js)
    js = re.sub(r' +', ' ', js)
    return '<script>' + js.strip() + '</script>'

html = re.sub(r'<script>((?!type="application/ld\+json").*?)</script>', minify_js, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Minified inline CSS and JS successfully")
