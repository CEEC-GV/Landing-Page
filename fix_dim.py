import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

services = ['consulting.webp', 'engineering.webp', 'cloud.webp', 'managed.webp']
for service in services:
    # replace width="1024" height="1024" with width="1194" height="880" only for these images
    pattern = r'(<img src="assets/images/' + re.escape(service) + r'"[^>]*)width="1024" height="1024"([^>]*>)'
    replacement = r'\g<1>width="1194" height="880"\g<2>'
    html = re.sub(pattern, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated dimensions")
