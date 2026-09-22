import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject Address into Contact Grid
address_html = '''        <div class="contact-info-item">
          <div class="icon-box"><svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></div>
          <div itemscope itemtype="https://schema.org/PostalAddress">
            <h4>Address</h4>
            <p><span itemprop="streetAddress">235, 13th Cross Rd, Indira Nagar</span><br><span itemprop="addressLocality">Bengaluru</span>, <span itemprop="addressRegion">Karnataka</span> <span itemprop="postalCode">560038</span></p>
          </div>
        </div>'''

# Find the last contact-info-item before the form and insert the address there
html = re.sub(
    r'(<div class="contact-info-item">.*?Working with clients and users across multiple countries and time zones\.</p></div>\s*</div>)',
    r'\1\n' + address_html,
    html,
    flags=re.DOTALL
)

# 2. Inject Address into Footer Contact column
footer_address = '''          <li style="margin-top:12px; line-height:1.4;">235, 13th Cross Rd<br>Indira Nagar, Bengaluru<br>Karnataka 560038</li>'''
html = re.sub(
    r'(<li><a href="tel:\+917899616501">\+91 78996 16501</a></li>)',
    r'\1\n' + footer_address,
    html
)

# 3. Inject Privacy and Terms links into footer-bottom
footer_bottom_replacement = '''    <div class="footer-bottom" style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:16px;">
      <span>© <span id="year"></span> CEEC Global Ventures. All rights reserved.</span>
      <div style="display:flex; gap:16px;">
        <a href="privacy.html" style="color:inherit; text-decoration:none;">Privacy Policy</a>
        <a href="terms.html" style="color:inherit; text-decoration:none;">Terms of Service</a>
      </div>
      <span>Made for a global, technology-first world.</span>
    </div>'''
html = re.sub(
    r'<div class="footer-bottom">.*?</div>',
    footer_bottom_replacement,
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with Address, Privacy, and Terms")
