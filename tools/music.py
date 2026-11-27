import numpy as np, wave, sys
sr=44100; out=sys.argv[1]; dur=float(sys.argv[2]); preset=sys.argv[3] if len(sys.argv)>3 else 'calm'
P={'calm':dict(bpm=76,prog=[[57,60,64],[53,57,60],[48,52,55,59],[55,59,62]],arp=8,oct=12,drums=0,bright=0.3,wave='sine'),
   'lofi':dict(bpm=84,prog=[[50,53,57,60],[55,59,62,65],[48,52,55,59],[57,60,64,67]],arp=4,oct=12,drums=1,bright=0.2,wave='sine'),
   'lift':dict(bpm=100,prog=[[48,52,55],[55,59,62],[57,60,64],[53,57,60]],arp=8,oct=24,drums=2,bright=0.5,wave='saw'),
   'tech':dict(bpm=92,prog=[[52,55,59],[48,52,55],[55,59,62],[50,54,57]],arp=16,oct=12,drums=1,bright=0.4,wave='square')}[preset]
beat=60/P['bpm']; bar=4*beat; n=int(sr*dur); mix=np.zeros(n)
def f(m): return 440*2**((m-69)/12)
def osc(fr,t,kind):
    s=np.sin(2*np.pi*fr*t)
    if kind=='saw': s=s+0.35*np.sin(4*np.pi*fr*t)+0.18*np.sin(6*np.pi*fr*t)
    if kind=='square': s=s+0.3*np.sin(6*np.pi*fr*t)+0.15*np.sin(10*np.pi*fr*t)
    return s
rng=np.random.default_rng(3)
for b in range(int(np.ceil(dur/bar))):
    ch=P['prog'][b%4]; s=int(b*bar*sr); e=min(n,int((b+1)*bar*sr)+int(0.6*sr))
    if s>=n: break
    tt=np.arange(e-s)/sr; env=np.minimum(1,tt/0.6)*np.exp(-np.maximum(0,tt-bar)/0.5)
    for m in ch:
        for det in (-0.1,0.1): mix[s:e]+=0.045*env*np.sin(2*np.pi*f(m+det)*tt)*(1+0.25*np.sin(2*np.pi*0.3*tt))
    mix[s:e]+=0.065*env*np.sin(2*np.pi*f(ch[0]-12)*tt)
    arp=ch+[ch[1]+12]; k_n=P['arp']; step=bar/k_n
    for k in range(k_n):
        st=s+int(k*step*sr); en=min(n,st+int(0.9*sr))
        if st>=n: break
        ta=np.arange(en-st)/sr; m=arp[k%len(arp)]+P['oct']
        mix[st:en]+=0.03*np.exp(-ta*(4 if k_n>8 else 3))*osc(f(m),ta,P['wave'])*(1+P['bright'])/1.4
    if P['drums']:
        for q in range(4):
            st=s+int(q*beat*sr)
            if st>=n: break
            if q in (0,2) or P['drums']==2:
                ln=min(n-st,int(0.25*sr)); ta=np.arange(ln)/sr
                mix[st:st+ln]+=0.11*np.exp(-ta*18)*np.sin(2*np.pi*(55+90*np.exp(-ta*30))*ta)
            hs=st+int(beat/2*sr); ln=min(n-hs,int(0.05*sr))
            if ln>0: mix[hs:hs+ln]+=0.012*rng.standard_normal(ln)*np.exp(-np.arange(ln)/sr*80)
rev=mix.copy()
for d,g in ((0.113,0.3),(0.171,0.25),(0.241,0.2),(0.337,0.15)):
    k=int(d*sr); rev[k:]+=g*mix[:-k]
rev=np.convolve(rev,np.ones(4)/4,'same')
fade=np.ones(n); fi=int(1.2*sr); fo=int(2.5*sr); fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
rev*=fade; rev/=np.max(np.abs(rev))+1e-9; rev*=0.45
st=np.stack([rev,np.roll(rev,int(0.012*sr))],1)
w=wave.open(out,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype('<i2').tobytes()); w.close()
