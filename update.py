import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace CSS
old_css = r'''  /\* ---------- Services \(list, not cards\) ---------- \*/
  \.bg-soft\{background:var\(--bg-soft\);\}
  \.service-list\{display:flex;flex-direction:column;border-top:1px solid var\(--border\);\}
  \.service-row\{
    display:grid;grid-template-columns:56px 230px 1fr;gap:28px;align-items:center;
    padding:30px 0;border-bottom:1px solid var\(--border\);
    transition:background \.15s ease;
  \}
  \.service-row:hover\{background:rgba\(27,47,128,0\.03\);\}
  \.service-row h3\{font-size:17px;margin:0;\}
  \.service-row p\{font-size:14\.5px;margin:0;\}'''

new_css = '''  /* ---------- Services (Cards Layout) ---------- */
  .bg-soft{background:var(--bg-soft);}
  .services-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    margin-top: 40px;
  }
  .service-card {
    background: #fff;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 12px 32px rgba(6,15,46,0.06);
    border: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .service-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(6,15,46,0.12);
  }
  .service-img-wrapper {
    position: relative;
    height: 200px;
  }
  .service-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .service-img-gradient {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 120px;
    background: linear-gradient(to bottom, rgba(255,255,255,0) 0%, rgba(255,255,255,1) 100%);
  }
  .service-content {
    padding: 0 24px 32px 24px;
    display: flex;
    flex-direction: column;
    flex: 1;
    position: relative;
    z-index: 2;
  }
  .service-content h3 {
    margin: 0 0 12px 0;
    font-size: 18px;
    color: var(--text);
  }
  .service-content p {
    margin: 0;
    font-size: 14.5px;
    color: var(--muted);
  }'''

html = re.sub(old_css, new_css, html)

# 2. Replace the HTML section
old_html_pattern = r'<section id="services" class="bg-soft">.*?<\/section>'

new_html = '''<section id="services" style="background:#fff;">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">What we do</span>
        <h2>Services built around your engineering needs</h2>
        <p>Whichever stage you're at — planning, building or running technology — we can plug in where it's most useful.</p>
      </div>
      <div class="services-grid">
        <div class="service-card">
          <div class="service-img-wrapper">
            <img src="assets/images/consulting.webp" alt="Technology consulting and architecture review" width="1024" height="1024" loading="lazy">
            <div class="service-img-gradient"></div>
          </div>
          <div class="service-content">
            <h3>Technology consulting</h3>
            <p>Architecture reviews, technology roadmaps and hands-on guidance for teams making big decisions.</p>
          </div>
        </div>
        
        <div class="service-card">
          <div class="service-img-wrapper">
            <img src="assets/images/engineering.webp" alt="Product engineering and development" width="1024" height="1024" loading="lazy">
            <div class="service-img-gradient"></div>
          </div>
          <div class="service-content">
            <h3>Product engineering</h3>
            <p>End-to-end design and development of web and mobile products, from first prototype to launch.</p>
          </div>
        </div>
        
        <div class="service-card">
          <div class="service-img-wrapper">
            <img src="assets/images/cloud.webp" alt="Cloud migrations and DevOps pipelines" width="1024" height="1024" loading="lazy">
            <div class="service-img-gradient"></div>
          </div>
          <div class="service-content">
            <h3>Cloud &amp; infrastructure</h3>
            <p>Cloud migrations, DevOps pipelines and infrastructure that stays stable as usage grows.</p>
          </div>
        </div>
        
        <div class="service-card">
          <div class="service-img-wrapper">
            <img src="assets/images/managed.webp" alt="Managed IT support and monitoring" width="1024" height="1024" loading="lazy">
            <div class="service-img-gradient"></div>
          </div>
          <div class="service-content">
            <h3>Managed support</h3>
            <p>Ongoing monitoring, maintenance and support so your systems keep running after launch.</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

html = re.sub(old_html_pattern, new_html, html, flags=re.DOTALL)

# Update responsive CSS for services-grid
html = re.sub(r'\.service-row\{grid-template-columns:1fr;gap:8px;\}', r'.services-grid { grid-template-columns: repeat(2, 1fr); gap: 16px; }', html)
# also add the mobile stack inside the 600px query
html = re.sub(r'\.cta-banner\{padding:32px;\}', r'.cta-banner{padding:32px;} .services-grid { grid-template-columns: 1fr; }', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
