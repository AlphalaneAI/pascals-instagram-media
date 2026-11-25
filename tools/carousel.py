import sys; sys.path.insert(0,'.')
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
W,H=1080,1350; INK=(18,20,26); IVORY=(250,248,243); GOLD=(184,146,60); MUTED=(90,90,96)
FD='/usr/share/fonts/opentype/inter/'
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
def cover(img,w,h,yb=0.3):
    r=max(w/img.width,h/img.height); img=img.resize((int(img.width*r)+1,int(img.height*r)+1),Image.LANCZOS)
    x=(img.width-w)//2; y=int((img.height-h)*yb); return img.crop((x,y,x+w,y+h))
out=sys.argv[1]
# 1 cover
im=cover(Image.open('cafe.png').convert('RGB'),W,H,0.0); 
ov=Image.new('L',(W,H),0); od=ImageDraw.Draw(ov)
for i in range(H): od.line([(0,i),(W,i)],fill=int(230*min(1,max(0,(i-760)/420))))
im=Image.composite(Image.new('RGB',(W,H),INK),im,ov); d=ImageDraw.Draw(im)
y=1010
for ln in wrap(d,'31 Jahre.',F('b',92),980): d.text((70,y),ln,font=F('b',92),fill=(224,199,122)); y+=104
for ln in wrap(d,'5 Dinge, die ich gern mit 21 gewusst hätte.',F('b',64),940): d.text((70,y),ln,font=F('b',64),fill=IVORY); y+=76
d.text((W-70,1290),'Wischen →',font=F('m',32),fill=(210,206,196),anchor='rs')
im.save(f'{out}/k1.jpg',quality=92)
items=[('«Später» ist kein Datum.','Ob Gesundheit, Familie oder Finanzen: Was du verschiebst, wird nicht einfacher. Nur dringender.'),
('Kleine Gewohnheiten schlagen grosse Vorsätze.','Ein Training pro Woche, das bleibt, bringt mehr als fünf, die du im Februar aufgibst. Beim Geld ist es genauso.'),
('Über Geld reden ist nicht unanständig.','Nicht darüber zu reden, kann dich am meisten kosten.'),
('Zeit mit meiner Familie kann ich nicht zurückkaufen.','Darum plane ich alles andere so, dass genau dafür Platz bleibt.'),
('Hilfe holen ist keine Schwäche.','Ob im Training, beim Bauen mit KI oder bei den Finanzen: Mit jemandem, der den Überblick hat, kommst du schneller weiter.')]
for i,(t,s) in enumerate(items):
    im=Image.new('RGB',(W,H),IVORY); d=ImageDraw.Draw(im)
    d.text((90,150),f'{i+1}',font=F('b',220),fill=(224,199,122))
    d.text((W-90,140),f'{i+2}/7',font=F('m',30),fill=MUTED,anchor='ra')
    y=470
    for ln in wrap(d,t,F('b',72),900): d.text((90,y),ln,font=F('b',72),fill=INK); y+=86
    y+=40; d.line([(90,y),(190,y)],fill=GOLD,width=6); y+=60
    for ln in wrap(d,s,F('m',44),900): d.text((90,y),ln,font=F('m',44),fill=(60,60,66)); y+=62
    d.text((90,1250),'@pascals.solutions',font=F('m',30),fill=MUTED)
    im.save(f'{out}/k{i+2}.jpg',quality=92)
# 7 closing with portrait circle
im=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(im)
p=cover(Image.open('portrait.png').convert('RGB'),420,420,0.1); m=Image.new('L',(420,420),0); ImageDraw.Draw(m).ellipse([0,0,419,419],fill=255)
im.paste(p,(330,170),m); d.ellipse([326,166,754,594],outline=(224,199,122),width=6)
y=690
for ln in wrap(d,'Welche Erkenntnis hättest du gern früher gehabt?',F('b',66),900): d.text((W/2,y),ln,font=F('b',66),fill=IVORY,anchor='ma'); y+=80
y+=30; d.text((W/2,y),'Schreib sie mir in die Kommentare ↓',font=F('m',40),fill=(224,199,122),anchor='ma'); y+=110
for ln in wrap(d,'Folg mir für mehr über Geld, Gesundheit & Familie.',F('m',40),860): d.text((W/2,y),ln,font=F('m',40),fill=(200,196,186),anchor='ma'); y+=56
im.save(f'{out}/k7.jpg',quality=92)
