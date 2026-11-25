# Story-Bild 1080x1920 aus JSON-Liste: python3 tools/story.py spec.json outdir
import sys, os, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W,H=1080,1920; INK=(18,20,26); IVORY=(250,248,243); GOLD=(212,178,84)
FD='/usr/share/fonts/opentype/inter/'; ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
def F(w,s): return ImageFont.truetype(FD+{'b':'InterDisplay-Bold.otf','m':'InterDisplay-Medium.otf','sb':'InterDisplay-SemiBold.otf'}[w],s)
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
for s in json.load(open(sys.argv[1])):
    if s.get('photo'):
        im=Image.open(os.path.join(ROOT,s['photo'])).convert('RGB'); r=max(W/im.width,H/im.height)
        im=im.resize((int(im.width*r)+1,int(im.height*r)+1)); x=(im.width-W)//2; im=im.crop((x,0,x+W,H))
        im=ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(6))).enhance(0.4)
    else: im=Image.new('RGB',(W,H),INK)
    d=ImageDraw.Draw(im)
    f=F('sb',38); tw=d.textlength(s['label'],font=f)
    d.rounded_rectangle([(W-tw)/2-28,300,(W+tw)/2+28,372],radius=36,fill=GOLD); d.text((W/2,336),s['label'],font=f,fill=INK,anchor='mm')
    y=s.get('y',470)
    for ln in wrap(d,s['t'],F('b',76),920): d.text((W/2,y),ln,font=F('b',76),fill=IVORY,anchor='ma'); y+=92
    y+=30
    for ln in wrap(d,s['sub'],F('m',46),900): d.text((W/2,y),ln,font=F('m',46),fill=(225,222,214),anchor='ma'); y+=62
    if s.get('fig'):
        fi=Image.open(os.path.join(ROOT,'assets','figuren','pose_'+s['fig']+'.png')).convert('RGBA'); h=660
        fi=fi.resize((int(fi.width*h/fi.height),h)); im.paste(fi,((W-fi.width)//2,H-h-250),fi)
    im.save(os.path.join(sys.argv[2],s['name']+'.jpg'),quality=92)
