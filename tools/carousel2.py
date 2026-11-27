# Generisches Karussell aus JSON: python3 tools/carousel2.py spec.json outdir prefix
import sys, os, json
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1350; INK=(18,20,26); IVORY=(250,248,243); GOLDL=(224,199,122); GOLD=(184,146,60); MUTED=(90,90,96)
FD='/usr/share/fonts/opentype/inter/'; ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
def F(w,s): return ImageFont.truetype(FD+{'b':'InterDisplay-Bold.otf','m':'InterDisplay-Medium.otf'}[w],s)
def wrap(d,t,f,mw):
    out=[]
    for p in t.split('\n'):
        c=''
        for w in p.split(' '):
            x=(c+' '+w).strip()
            if d.textlength(x,font=f)<=mw: c=x
            else: out.append(c); c=w
        out.append(c)
    return out
def cover(img,w,h,yb=0.3):
    r=max(w/img.width,h/img.height); img=img.resize((int(img.width*r)+1,int(img.height*r)+1),Image.LANCZOS)
    x=(img.width-w)//2; y=int((img.height-h)*yb); return img.crop((x,y,x+w,y+h))
def pose(n,h):
    fi=Image.open(os.path.join(ROOT,'assets','figuren','pose_'+n+'.png')).convert('RGBA'); return fi.resize((int(fi.width*h/fi.height),h),Image.LANCZOS)
spec=json.load(open(sys.argv[1])); out=sys.argv[2]; pre=sys.argv[3]; os.makedirs(out,exist_ok=True)
N=len(spec['items'])+2; c=spec['cover']
im=cover(Image.open(os.path.join(ROOT,c['photo'])).convert('RGB'),W,H,c.get('yb',0.0))
ov=Image.new('L',(W,H),0); od=ImageDraw.Draw(ov)
for i in range(H): od.line([(0,i),(W,i)],fill=int(230*min(1,max(0,(i-720)/420))))
im=Image.composite(Image.new('RGB',(W,H),INK),im,ov); d=ImageDraw.Draw(im); y=c.get('y',990)
for ln in wrap(d,c['kicker'],F('b',84),980): d.text((70,y),ln,font=F('b',84),fill=GOLDL); y+=96
for ln in wrap(d,c['title'],F('b',62),940): d.text((70,y),ln,font=F('b',62),fill=IVORY); y+=74
d.text((W-70,1300),'Wischen →',font=F('m',32),fill=(210,206,196),anchor='rs'); im.save(f'{out}/{pre}-1.jpg',quality=92)
for i,it in enumerate(spec['items']):
    im=Image.new('RGB',(W,H),IVORY); d=ImageDraw.Draw(im)
    d.text((90,150),str(i+1),font=F('b',200),fill=GOLDL); d.text((W-90,140),f'{i+2}/{N}',font=F('m',30),fill=MUTED,anchor='ra')
    tw=900 if not it.get('fig') else 600; y=440
    for ln in wrap(d,it['t'],F('b',66),tw): d.text((90,y),ln,font=F('b',66),fill=INK); y+=80
    y+=36; d.line([(90,y),(190,y)],fill=GOLD,width=6); y+=56
    for ln in wrap(d,it['s'],F('m',42),tw): d.text((90,y),ln,font=F('m',42),fill=(60,60,66)); y+=58
    if it.get('fig'):
        fi=pose(it['fig'],720); im.paste(fi,(W-fi.width-40,H-fi.height-60),fi)
    d.text((90,1250),'@pascals.solutions',font=F('m',30),fill=MUTED); im.save(f'{out}/{pre}-{i+2}.jpg',quality=92)
e=spec['end']; im=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(im)
p=cover(Image.open(os.path.join(ROOT,e['photo'])).convert('RGB'),420,420,0.1); m=Image.new('L',(420,420),0); ImageDraw.Draw(m).ellipse([0,0,419,419],fill=255)
im.paste(p,(330,170),m); d.ellipse([326,166,754,594],outline=GOLDL,width=6); y=690
for ln in wrap(d,e['title'],F('b',64),900): d.text((W/2,y),ln,font=F('b',64),fill=IVORY,anchor='ma'); y+=78
y+=30
for ln in wrap(d,e['sub'],F('m',40),880): d.text((W/2,y),ln,font=F('m',40),fill=GOLDL,anchor='ma'); y+=54
y+=50
for ln in wrap(d,e['cta'],F('m',38),860): d.text((W/2,y),ln,font=F('m',38),fill=(200,196,186),anchor='ma'); y+=52
im.save(f'{out}/{pre}-{N}.jpg',quality=92)
