import sys,glob,re,os
from playwright.sync_api import sync_playwright
files=sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates', '*.html')))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':900,'height':1200})
    for f in files:
        src=open(f).read()
        dd=src.count('<div')-src.count('</div>')
        tv=src.count('—'); bl=len(re.findall(r'border-left:[^;]*(#|var\(--b)',src))
        pg.goto('file://'+os.path.abspath(f)); pg.wait_for_timeout(1500)
        r=pg.evaluate('''()=>[...document.querySelectorAll('.pg')].map((p,i)=>{var b=p.querySelector('.body');if(!b)return {i:i+1,cover:1};var fl=b.querySelector('.fill');var bb=b.getBoundingClientRect(),fr=fl.getBoundingClientRect();return {i:i+1,h:Math.round(p.getBoundingClientRect().height),over:Math.round(fl.scrollHeight-b.clientHeight),fill:Math.round(fl.getBoundingClientRect().height/b.clientHeight*100)}})''')
        print(f.split('/')[-1], 'div_diff',dd,'trav',tv,'bleft',bl)
        for x in r: print('   ',x)
    b.close()
