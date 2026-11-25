import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
names={'bogenA':['zeigt_links','zeigt_rechts','idee','nachdenklich','schulterzucken','ueberrascht','stopp','winkt'],
       'bogenB':['hantel','joggen','laptop','blazer_dokument','sparschwein','smartphone','winter_kaffee','papa_kind']}
for sheet,nm in names.items():
    im=np.array(Image.open(sheet+'.png').convert('RGB')).astype(int)
    r,g,b=im[...,0],im[...,1],im[...,2]
    mag=(r>170)&(b>170)&(g<110)&(abs(r-b)<70)
    fg=ndimage.binary_opening(~mag,iterations=1)
    lab,n=ndimage.label(ndimage.binary_dilation(fg,iterations=6))
    sizes=ndimage.sum(np.ones_like(lab),lab,range(1,n+1))
    comps=[i+1 for i in np.argsort(-sizes)[:8]]
    boxes=[]
    for c in comps:
        ys,xs=np.where(lab==c); boxes.append((ys.min(),ys.max(),xs.min(),xs.max(),c))
    boxes.sort(key=lambda b:(0 if (b[0]+b[1])/2<im.shape[0]/2 else 1, b[2]))
    alpha=np.array(Image.fromarray(np.where(fg,255,0).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)))
    rgb=im.copy(); spill=mag|(alpha<250)
    rgb[...,0]=np.where(spill,np.minimum(r,g+60),r); rgb[...,2]=np.where(spill,np.minimum(b,g+60),b)
    full=np.dstack([rgb.clip(0,255).astype(np.uint8),alpha])
    for (y0,y1,x0,x1,c),name in zip(boxes,nm):
        m=(lab[y0:y1+1,x0:x1+1]==c); crop=full[y0:y1+1,x0:x1+1].copy(); crop[...,3]=np.where(m,crop[...,3],0)
        Image.fromarray(crop).save(name+'.png')
    print(sheet,n,[int(s) for s in sorted(sizes,reverse=True)[:10]])
order=sum(names.values(),[])
sheet=Image.new('RGB',(1600,700),(30,32,40))
for i,f in enumerate(order):
    im=Image.open(f+'.png'); im.thumbnail((190,330)); sheet.paste(im,((i%8)*200+5,(i//8)*350+5),im)
sheet.save('../check4.png')
