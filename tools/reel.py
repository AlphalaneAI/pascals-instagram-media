import json, sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
W,H=1080,1920
INK=(18,20,26); IVORY=(250,248,243); GOLD=(212,178,84)
FD='/usr/share/fonts/opentype/inter/'
def font(w,s): return ImageFont.truetype(FD+{'b':'InterDisplay-Bold.otf','sb':'InterDisplay-SemiBold.otf','m':'InterDisplay-Medium.otf'}[w],s)
def wrap(d,text,f,maxw):
    lines=[]
    for para in text.split('\n'):
        cur=''
        for wd in para.split(' '):
            tst=(cur+' '+wd).strip()
            if d.textlength(tst,font=f)<=maxw: cur=tst
            else: lines.append(cur); cur=wd
        lines.append(cur)
    return lines
def cover(img,w,h):
    r=max(w/img.width,h/img.height); img=img.resize((int(img.width*r)+1,int(img.height*r)+1),Image.LANCZOS)
    x=(img.width-w)//2; y=max(0,int((img.height-h)*0.35)); return img.crop((x,y,x+w,y+h))
def bg(spec):
    if spec.get('bg'):
        im=cover(Image.open(spec['bg']).convert('RGB'),W,H)
        im=im.filter(ImageFilter.GaussianBlur(spec.get('blur',0)))
        im=ImageEnhance.Brightness(im).enhance(spec.get('dim',0.42))
        if not spec.get('grad',True): return im
        ov=Image.new('L',(W,H),0); od=ImageDraw.Draw(ov)
        for i in range(H):
            a=int(235*min(1,max(0,(i-620)/520))); od.line([(0,i),(W,i)],fill=a)
        im=Image.composite(Image.new('RGB',(W,H),INK),im,ov)
        return im
    im=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(im)
    for i in range(H):  # subtle vertical gradient
        c=tuple(int(INK[k]+(30-INK[k])*0.25*(i/H)) for k in range(3)); d.line([(0,i),(W,i)],fill=c)
    return im
def slide(spec,s,path):
    im=bg(spec).copy(); d=ImageDraw.Draw(im)
    if spec.get('label'):
        f=font('sb',38); tw=d.textlength(spec['label'],font=f)
        d.rounded_rectangle([(W-tw)/2-28,250,(W+tw)/2+28,322],radius=36,fill=GOLD)
        d.text((W/2,286),spec['label'],font=f,fill=INK,anchor='mm')
    size=s.get('size',74); f=font('b',size); lines=wrap(d,s['t'],f,900)
    lh=int(size*1.22); sub=s.get('sub'); fs=font('m',int(size*0.62)); sl=wrap(d,sub,fs,880) if sub else []
    slh=int(size*0.62*1.35); total=len(lines)*lh+(40+len(sl)*slh if sl else 0)
    fig=s.get('fig')
    if fig:
        fp=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','assets','figuren','pose_'+fig+'.png')
        fi=Image.open(fp).convert('RGBA'); fh=s.get('fh',820); fi=fi.resize((int(fi.width*fh/fi.height),fh),Image.LANCZOS)
        if fi.width>980: fi=fi.resize((980,int(fi.height*980/fi.width)),Image.LANCZOS)
        im.paste(fi,(int((W-fi.width)/2),1120+820-fi.height-80),fi)
    y=(s.get('cy') or (640 if fig else spec.get('cy',860)))-total//2
    hl=s.get('hl',[])
    for ln in lines:
        col=GOLD if any(h in ln for h in hl) else IVORY
        d.text((W/2+3,y+3),ln,font=f,fill=(0,0,0),anchor='ma')
        d.text((W/2,y),ln,font=f,fill=col,anchor='ma'); y+=lh
    if sl:
        y+=40
        for ln in sl: d.text((W/2,y),ln,font=fs,fill=(225,222,214),anchor='ma'); y+=slh
    hy=360 if fig else spec.get('hy',1430)
    if s.get('note') and fig: d.text((W/2,y+30),s['note'],font=font('m',28),fill=(170,166,158),anchor='ma')
    d.text((W/2,hy),'@pascals.solutions',font=font('m',34),fill=(200,196,186),anchor='ma')
    if s.get('note') and not fig: d.text((W/2,spec.get('hy',1430)+60),s['note'],font=font('m',28),fill=(170,166,158),anchor='ma')
    im.save(path)
spec=json.load(open(sys.argv[1])); out=sys.argv[2]; tmp=out+'_tmp'; os.makedirs(tmp,exist_ok=True)
durs=[]; fps=30; xf=0.35
for i,s in enumerate(spec['slides']):
    p=f'{tmp}/{i:02d}.png'; slide(spec,s,p)
    d=s.get('d', round(min(5.5,max(2.4,1.4+len(s['t']+s.get('sub',''))*0.045)),2)); durs.append(d)
    fr=int((d+xf)*fps)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-i',p,'-vf',
      f"scale=1188:2112,zoompan=z='1+0.035*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s={W}x{H}:fps={fps},format=yuv420p",
      '-frames:v',str(fr),'-c:v','libx264','-preset','veryfast','-crf','18',f'{tmp}/{i:02d}.mp4'],check=True)
n=len(durs); inputs=[]; 
for i in range(n): inputs+=['-i',f'{tmp}/{i:02d}.mp4']
fc=''; prev='[0:v]'; off=0
for i in range(1,n):
    off+=durs[i-1]; fc+=f"{prev}[{i}:v]xfade=transition=fade:duration={xf}:offset={off:.3f}[v{i}];"; prev=f'[v{i}]'
total=sum(durs)+xf
subprocess.run(['python3',os.path.dirname(__file__)+'/music.py',tmp+'/m.wav',str(total+0.5),spec.get('music','calm')],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error',*inputs,'-i',tmp+'/m.wav','-filter_complex',fc.rstrip(';'),'-map',prev,'-map',f'{n}:a',
  '-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',out],check=True)
print(out, round(total,1),'s')
