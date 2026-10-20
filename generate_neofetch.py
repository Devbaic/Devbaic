import cv2, numpy as np, base64, html, os, sys
from PIL import Image
e=html.escape
SRC=os.path.join(os.path.dirname(os.path.abspath(__file__)),'me.jpg')
OUT=os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT,exist_ok=True)

# ===== EDIT ME =====
USER="luy"; HOST="shadow-monarch"
INFO=[
 ("Name","Luy"),("Country","Cambodia"),("Role","Student & Full Stack Developer"),
 ("Title","Shadow Monarch Developer"),("Passion","Building Powerful Applications"),
 ("Languages","ខ្មែរ, English"),
 "SEC:Training",
 ("Learning","Microservices Architecture"),("","Docker & Cloud Systems"),("","Backend Engineering"),("","System Design"),
 "SEC:Stack",
 ("Code","PHP · JavaScript · TypeScript · SQL"),("Frameworks","Laravel · React · Tailwind"),
 ("DevOps","Docker · Linux · Nginx · AWS"),("Tools","Git · Postman · VS Code"),
 "SEC:Main Quest",
 ("Quest","Become Elite Software Engineer"),
 "SEC:Contact",
 ("GitHub","github.com/YOUR_USERNAME"),("Telegram","@YOUR_HANDLE"),("Email","your@email.com"),
]
LEVEL=24; HP,MP,EXP=92,74,63
# ===================

THEMES={
 "shadow":dict(a="#a855f7",b="#6366f1",c="#e879f9",bg1="#07060f",bg2="#150b2e",dim="#3b1d6e"),
 "blood": dict(a="#ef4444",b="#f97316",c="#fb7185",bg1="#0b0506",bg2="#2a0a0f",dim="#6e1d1d"),
 "arise": dict(a="#22d3ee",b="#3b82f6",c="#67e8f9",bg1="#050a10",bg2="#071c2e",dim="#0e4a6e"),
}
RAMP=" .,:;-~=+*xX#%@"

# ---------- image prep ----------
img=cv2.imread(SRC)[0:640,70:570]            # 500x640
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cl=cv2.createCLAHE(clipLimit=4.0,tileGridSize=(6,6))
lab[:,:,0]=cl.apply(lab[:,:,0])
lift=cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
hsv=cv2.cvtColor(lift,cv2.COLOR_BGR2HSV).astype(float)
hsv[:,:,2]=255*(hsv[:,:,2]/255)**0.62
hsv[:,:,1]=np.clip(hsv[:,:,1]*1.1,0,255)
bright=cv2.cvtColor(hsv.astype('uint8'),cv2.COLOR_HSV2BGR)
# subject mask: background = saturated red hue
hsv0=cv2.cvtColor(bright,cv2.COLOR_BGR2HSV)
hh,ss=hsv0[:,:,0].astype(int),hsv0[:,:,1].astype(int)
bg=(((hh>=168)|(hh<=2))&(ss>165)).astype('uint8')*255
bg=cv2.GaussianBlur(bg,(0,0),2); bg=(bg>110).astype('uint8')*255
bg=cv2.morphologyEx(bg,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
subj=255-bg
subj=cv2.morphologyEx(subj,cv2.MORPH_CLOSE,np.ones((25,25),np.uint8))
subj=cv2.morphologyEx(subj,cv2.MORPH_OPEN,np.ones((9,9),np.uint8))
n,lbl,st,_=cv2.connectedComponentsWithStats(subj)
if n>1:
    k=1+np.argmax(st[1:,cv2.CC_STAT_AREA]); subj=((lbl==k)*255).astype('uint8')
m=cv2.GaussianBlur(subj,(0,0),3)/255.0
COLS=82; CW=5.6; CH=10.6
ROWS=int(img.shape[0]/img.shape[1]*COLS*CW/CH)
small=cv2.resize(bright,(COLS,ROWS),interpolation=cv2.INTER_AREA)
smask=cv2.resize(m,(COLS,ROWS),interpolation=cv2.INTER_AREA)
g0=cv2.cvtColor(bright,cv2.COLOR_BGR2GRAY).astype(float)
g0=cv2.addWeighted(g0,1.8,cv2.GaussianBlur(g0,(0,0),6),-0.8,0)
sl=cv2.resize(g0,(COLS,ROWS),interpolation=cv2.INTER_AREA)
sel=smask>0.5
lo,hi=np.percentile(sl[sel],3),np.percentile(sl[sel],99)
sl=np.clip((sl-lo)/(hi-lo),0,1)
sl=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(4,4)).apply((sl*255).astype('uint8'))/255.0
sl=sl**0.85

def hex2rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def mix(c1,c2,t):
    a,b=hex2rgb(c1),hex2rgb(c2); return '#%02x%02x%02x'%tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))

PX,PY=34,48           # portrait origin
PW,PH=COLS*CW,ROWS*CH
W=1000; H=max(int(PY+PH+46),700)

def defs(T):
    return f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{T['bg1']}"/><stop offset="1" stop-color="{T['bg2']}"/></linearGradient>
<linearGradient id="tx" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{T['c']}"/><stop offset="1" stop-color="{T['a']}"/></linearGradient>
<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{T['b']}"/><stop offset="1" stop-color="{T['c']}"/></linearGradient>
<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{T['a']}" stop-opacity="0"/><stop offset=".5" stop-color="{T['c']}" stop-opacity=".35"/><stop offset="1" stop-color="{T['a']}" stop-opacity="0"/></linearGradient>
<radialGradient id="gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{T['a']}" stop-opacity=".35"/><stop offset="1" stop-color="{T['a']}" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{T['a']}" stroke-opacity=".07"/></pattern>
<clipPath id="pclip"><rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="8"/></clipPath>
</defs>
<style>text{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono','Noto Sans Khmer',monospace}}.k{{fill:{T['c']};font-weight:700}}.w{{fill:#e5e7eb}}.m{{fill:#8b93a1}}</style>'''

def frame(T):
    s=f'<rect width="{W}" height="{H}" rx="14" fill="url(#bg)"/><rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>'
    s+=f'<ellipse cx="{PX+PW/2}" cy="{PY+PH/2}" rx="{PW*.6}" ry="{PH*.55}" fill="url(#gl)"><animate attributeName="opacity" values=".5;1;.5" dur="4s" repeatCount="indefinite"/></ellipse>'
    s+=f'<rect x="8" y="8" width="{W-16}" height="{H-16}" rx="10" fill="none" stroke="{T["a"]}" stroke-opacity=".45"><animate attributeName="stroke-opacity" values=".2;.7;.2" dur="3.5s" repeatCount="indefinite"/></rect>'
    # window dots + title
    for i,c in enumerate(["#ff5f56","#ffbd2e","#27c93f"]): s+=f'<circle cx="{26+i*18}" cy="24" r="5" fill="{c}"/>'
    s+=f'<text x="{W/2}" y="28" text-anchor="middle" font-size="12" letter-spacing="3" class="m">{USER}@{HOST}: ~ — neofetch</text>'
    return s

def info(T):
    x=PX+PW+40; y=PY+8; s=''; d=0.3
    s+=f'<g opacity="0"><animate attributeName="opacity" to="1" dur=".4s" begin="{d}s" fill="freeze"/><text x="{x}" y="{y}" font-size="17" font-weight="800" filter="url(#glow)"><tspan fill="{T["c"]}">{USER}</tspan><tspan class="w">@</tspan><tspan fill="{T["a"]}">{HOST}</tspan></text></g>'
    y+=10; d+=.1
    s+=f'<line x1="{x}" y1="{y}" x2="{x+0}" y2="{y}" stroke="{T["a"]}" stroke-opacity=".7"><animate attributeName="x2" from="{x}" to="{W-40}" dur="1s" begin="{d}s" fill="freeze"/></line>'
    y+=24
    for it in INFO:
        d+=.09
        if isinstance(it,str):
            y+=8
            s+=f'<g opacity="0"><animate attributeName="opacity" to="1" dur=".3s" begin="{d}s" fill="freeze"/><text x="{x}" y="{y}" font-size="12" letter-spacing="3" class="m">◆ {e(it[4:].upper())}</text><line x1="{x+12+len(it[4:])*10}" y1="{y-4}" x2="{W-40}" y2="{y-4}" stroke="{T["a"]}" stroke-opacity=".25"/></g>'
            y+=20; continue
        k,v=it
        s+=f'<g opacity="0"><animate attributeName="opacity" to="1" dur=".3s" begin="{d}s" fill="freeze"/><text x="{x}" y="{y}" font-size="13.5"><tspan class="k">{e(k) if k else "":<0}</tspan></text><text x="{x+112}" y="{y}" font-size="13.5" class="w">{e(v)}</text></g>'
        if k: s=s.replace(f'<tspan class="k">{e(k)}</tspan></text><text x="{x+112}" y="{y}"',f'<tspan class="k">{e(k)}</tspan></text><text x="{x+112}" y="{y}"')
        y+=19
    # stat bars
    y+=10
    bars=[("LV",LEVEL,100),("HP",HP,100),("MP",MP,100),("EXP",EXP,100)]
    bw=(W-40-x-30)/2
    for i,(n,v,_) in enumerate(bars):
        bx=x+(i%2)*(bw+30); by=y+(i//2)*26
        s+=f'<text x="{bx}" y="{by}" font-size="11" letter-spacing="2" class="m">{n} <tspan class="k">{v}</tspan></text>'
        s+=f'<rect x="{bx+62}" y="{by-9}" width="{bw-62}" height="8" rx="4" fill="#fff" fill-opacity=".08"/><rect x="{bx+62}" y="{by-9}" width="0" height="8" rx="4" fill="url(#bar)" filter="url(#glow)"><animate attributeName="width" from="0" to="{(bw-62)*v/100:.1f}" dur="1.4s" begin="{d+.2+i*.15}s" fill="freeze"/></rect>'
    y+=62
    cols=[T['c'],T['a'],T['b'],"#f85149","#d29922","#3fb950","#39c5cf","#c9d1d9"]
    for i,c in enumerate(cols):
        s+=f'<rect x="{x+i*30}" y="{y}" width="26" height="14" rx="3" fill="{c}"><animate attributeName="opacity" values="1;.55;1" dur="{2+i*.3:.1f}s" repeatCount="indefinite"/></rect>'
    s+=f'<text x="{x}" y="{y+38}" font-size="14" class="k">❯ <tspan class="w">arise</tspan><tspan fill="{T["c"]}">█<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></tspan></text>'
    return s

def corners(T,p=PX-6,q=PY-6,w=PW+12,h=PH+12,l=22):
    s=''
    for X,Y,dx,dy in [(p,q,1,1),(p+w,q,-1,1),(p,q+h,1,-1),(p+w,q+h,-1,-1)]:
        s+=f'<path d="M{X} {Y+dy*l}V{Y}H{X+dx*l}" fill="none" stroke="{T["c"]}" stroke-width="2.4" filter="url(#glow)"/>'
    return s
def scan(T):
    return f'<g clip-path="url(#pclip)"><rect x="{PX}" y="{PY-60}" width="{PW}" height="60" fill="url(#scan)"><animate attributeName="y" values="{PY-60};{PY+PH}" dur="4.5s" repeatCount="indefinite"/></rect></g>'

def rowtext(r):  # returns list of (x_index,char,color) for variant builders
    pass

def v_mono(T):
    s=''
    for r in range(ROWS):
        spans=''
        for c in range(COLS):
            t=sl[r,c]*smask[r,c]
            if t<0.03: spans+=' '; continue
            ch=RAMP[min(int(t*len(RAMP)),len(RAMP)-1)]
            col=mix(T['b'],T['c'],t/.6) if t<.6 else mix(T['c'],'#ffffff',(t-.6)/.4)
            spans+=f'<tspan fill="{col}">{e(ch)}</tspan>'
        s+=f'<text x="{PX}" y="{PY+r*CH+CH-2}" font-size="9.4" textLength="{PW}" lengthAdjust="spacing" xml:space="preserve" opacity="0">{spans}<animate attributeName="opacity" to="1" dur=".3s" begin="{.2+r*.025:.2f}s" fill="freeze"/></text>'
    return s
def q(v): return int(round(v/24.0))*24
def v_color(T):
    s=''
    for r in range(ROWS):
        spans=''
        for c in range(COLS):
            t=sl[r,c]; mk=smask[r,c]
            bb,gg,rr=[int(x) for x in small[r,c]]
            tt=max(t,0.0)
            if tt<0.05: spans+=' '; continue
            ch=RAMP[min(int(tt*len(RAMP)),len(RAMP)-1)]
            # background: keep dim themed tint, subject: real colour
            if mk<.5:
                col=mix(T['bg2'],T['dim'],min(1,tt*2))
            else:
                k=1.18; col='#%02x%02x%02x'%(min(255,q(rr*k)),min(255,q(gg*k)),min(255,q(bb*k)))
            spans+=f'<tspan fill="{col}">{e(ch)}</tspan>'
        s+=f'<text x="{PX}" y="{PY+r*CH+CH-2}" font-size="9.4" textLength="{PW}" lengthAdjust="spacing" xml:space="preserve" opacity="0">{spans}<animate attributeName="opacity" to="1" dur=".3s" begin="{.2+r*.025:.2f}s" fill="freeze"/></text>'
    return s
def v_dots(T):
    s=''
    for r in range(ROWS):
        for c in range(COLS):
            t=sl[r,c]*smask[r,c]
            if t<0.06: continue
            rad=0.6+2.5*t**0.8
            col=mix(T['b'],T['c'],t) if t<.7 else mix(T['c'],'#ffffff',(t-.7)/.3)
            s+=f'<circle cx="{PX+c*CW+CW/2:.1f}" cy="{PY+r*CH+CH/2:.1f}" r="{rad:.2f}" fill="{col}" opacity="0"><animate attributeName="opacity" to="{0.55+0.45*t:.2f}" dur=".3s" begin="{.2+r*.025+c*.002:.2f}s" fill="freeze"/></circle>'
    return s
def v_photo(T):
    pic=cv2.resize(bright,(int(PW),int(PH)),interpolation=cv2.INTER_AREA)
    ok,buf=cv2.imencode('.jpg',pic,[cv2.IMWRITE_JPEG_QUALITY,82])
    b64=base64.b64encode(buf).decode()
    s=f'<image x="{PX}" y="{PY}" width="{PW}" height="{PH}" clip-path="url(#pclip)" href="data:image/jpeg;base64,{b64}" preserveAspectRatio="xMidYMid slice" opacity="0"><animate attributeName="opacity" to="1" dur="1.2s" begin=".2s" fill="freeze"/></image>'
    # duotone-ish overlay + scanlines
    s+=f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="8" fill="{T["a"]}" opacity=".12" style="mix-blend-mode:color"/>'
    lines=''.join(f'<line x1="{PX}" y1="{PY+i}" x2="{PX+PW}" y2="{PY+i}"/>' for i in range(0,int(PH),4))
    s+=f'<g clip-path="url(#pclip)" stroke="#000" stroke-opacity=".18">{lines}</g>'
    s+=f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="8" fill="none" stroke="{T["a"]}" stroke-width="1.5" filter="url(#glow)"/>'
    return s

VARIANTS={"mono":v_mono,"color":v_color,"dots":v_dots,"photo":v_photo}
def build(vn,tn):
    T=THEMES[tn]
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{defs(T)}{frame(T)}{VARIANTS[vn](T)}{scan(T)}{corners(T)}{info(T)}</svg>'
    open(f'{OUT}/{vn}-{tn}.svg','w',encoding='utf-8').write(svg)
if __name__=='__main__':
    vs=sys.argv[1:2] or list(VARIANTS); ts=sys.argv[2:3] or list(THEMES)
    for v in (vs if vs!=['all'] else VARIANTS):
        for t in (ts if ts!=['all'] else THEMES): build(v,t)
    print(W,H,COLS,ROWS)
