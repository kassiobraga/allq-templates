import glob,os
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':794,'height':1123})
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates', '*.html'))):
        pg.goto('file://'+os.path.abspath(f)); pg.wait_for_timeout(1500)
        pg.pdf(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pdf', '')+f.split('/')[-1].replace('.html','.pdf'),prefer_css_page_size=True,print_background=True)
    b.close()
