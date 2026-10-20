# Run: python3 generate.py [shadow|blood|arise]   -> rewrites header.svg, status.svg, quest.svg, footer.svg
import sys, random, html
random.seed(7)

# ============ EDIT ME ============
NAME   = "LUY"
ROLE   = "STUDENT & FULL STACK DEVELOPER"
TITLE  = "Shadow Monarch Developer"
COUNTRY= "CAMBODIA"
PASSION= "Building Powerful Applications"
MAIN_QUEST = "Become Elite Software Engineer"
LEVEL  = 24
STATS  = [("BACKEND",82),("SYSTEM DESIGN",68),("FRONTEND",75),("DEVOPS / DOCKER",64),("CLOUD",58),("DEBUGGING",85)]
TRAINING=[("Microservices Architecture",55),("Docker & Cloud Systems",62),("Backend Engineering",78),("System Design",60)]
QUESTS = ["Building Full Stack Projects","Learning Cloud Infrastructure","Exploring Scalable Systems","Improving Coding Skills","Creating Legendary Applications"]
HP, MP, EXP = 92, 74, 63
# =================================

THEMES = {
 "shadow": dict(a="#a855f7", b="#6366f1", c="#e879f9", bg1="#07060f", bg2="#150b2e"),
 "blood":  dict(a="#ef4444", b="#f97316", c="#fb7185", bg1="#0b0506", bg2="#2a0a0f"),
 "arise":  dict(a="#22d3ee", b="#3b82f6", c="#67e8f9", bg1="#050a10", bg2="#071c2e"),
}
T = THEMES[sys.argv[1] if len(sys.argv)>1 else "shadow"]
A,B,C,BG1,BG2 = T["a"],T["b"],T["c"],T["bg1"],T["bg2"]
FONT = "'Segoe UI','Courier New',monospace"
e = html.escape

def defs(w,h):
    return f'''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG2}"/></linearGradient>
<linearGradient id="tx" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{C}"/><stop offset=".5" stop-color="#ffffff"/><stop offset="1" stop-color="{A}"/></linearGradient>
<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{B}"/><stop offset="1" stop-color="{C}"/></linearGradient>
<radialGradient id="gl" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{A}" stop-opacity=".45"/><stop offset="1" stop-color="{A}" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" fill="none" stroke="{A}" stroke-opacity=".08"/></pattern>
</defs>
<style>text{{font-family:{FONT}}} .m{{fill:#9ca3af}} .w{{fill:#e5e7eb}} .k{{fill:{C};font-weight:700}}</style>'''

def corners(w,h,p=14,l=26):
    s=""
    for x,y,dx,dy in [(p,p,1,1),(w-p,p,-1,1),(p,h-p,1,-1),(w-p,h-p,-1,-1)]:
        s+=f'<path d="M{x} {y+dy*l}V{y}H{x+dx*l}" fill="none" stroke="{A}" stroke-width="2.5" filter="url(#glow)"/>'
    return s

def bar(x,y,w,val,label,delay=0.3,color="url(#bar)"):
    return f'''<text x="{x}" y="{y-8}" class="w" font-size="12" letter-spacing="1.5">{e(label)}</text>
<text x="{x+w}" y="{y-8}" class="k" font-size="12" text-anchor="end">{val}</text>
<rect x="{x}" y="{y}" width="{w}" height="9" rx="4.5" fill="#ffffff" fill-opacity=".07"/>
<rect x="{x}" y="{y}" width="0" height="9" rx="4.5" fill="{color}" filter="url(#glow)"><animate attributeName="width" from="0" to="{w*val/100:.1f}" dur="1.4s" begin="{delay}s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></rect>'''

# ---------------- HEADER ----------------
def header():
    w,h=900,280
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{defs(w,h)}'
    s+=f'<rect width="{w}" height="{h}" rx="14" fill="url(#bg)"/><rect width="{w}" height="{h}" rx="14" fill="url(#grid)"/>'
    s+=f'<ellipse cx="450" cy="130" rx="380" ry="120" fill="url(#gl)"><animate attributeName="opacity" values=".55;1;.55" dur="4s" repeatCount="indefinite"/></ellipse>'
    for i in range(34):
        x=random.randint(20,880); y=random.randint(60,270); r=random.choice([1,1.3,1.8,2.4]); d=random.uniform(4,9)
        s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{random.choice([A,C,"#fff"])}" opacity="0"><animate attributeName="cy" values="{y};{y-70}" dur="{d:.1f}s" repeatCount="indefinite" begin="{random.uniform(0,5):.1f}s"/><animate attributeName="opacity" values="0;.9;0" dur="{d:.1f}s" repeatCount="indefinite" begin="{random.uniform(0,5):.1f}s"/></circle>'
    s+=f'<text x="450" y="50" text-anchor="middle" font-size="13" letter-spacing="8" class="m">[ SYSTEM  NOTIFICATION ]</text>'
    s+=f'<text x="450" y="135" text-anchor="middle" font-size="62" font-weight="900" letter-spacing="6" fill="url(#tx)" filter="url(#glow)">SHADOW MONARCH<animate attributeName="opacity" values="1;.82;1" dur="3s" repeatCount="indefinite"/></text>'
    s+=f'<line x1="200" y1="158" x2="700" y2="158" stroke="{A}" stroke-opacity=".6"><animate attributeName="x2" values="200;700" dur="1.6s" fill="freeze"/></line>'
    s+=f'<text x="450" y="192" text-anchor="middle" font-size="22" letter-spacing="5" class="w">{e(NAME)}  //  {e(ROLE)}</text>'
    s+=f'<clipPath id="tp"><rect x="150" y="212" width="0" height="40"><animate attributeName="width" from="0" to="600" dur="2.6s" begin="0.6s" fill="freeze"/></rect></clipPath>'
    s+=f'<text x="450" y="238" text-anchor="middle" font-size="15" letter-spacing="3" class="k" clip-path="url(#tp)">&gt; {e(COUNTRY)}  ·  {e(PASSION.upper())}</text>'
    s+=corners(w,h)+'</svg>'
    return s

# ---------------- STATUS ----------------
def status():
    w,h=900,470
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{defs(w,h)}'
    s+=f'<rect width="{w}" height="{h}" rx="14" fill="url(#bg)"/><rect width="{w}" height="{h}" rx="14" fill="url(#grid)"/>'
    s+=f'<rect x="10" y="10" width="{w-20}" height="{h-20}" rx="10" fill="none" stroke="{A}" stroke-opacity=".5"><animate attributeName="stroke-opacity" values=".25;.8;.25" dur="3.5s" repeatCount="indefinite"/></rect>'
    s+=f'<rect x="10" y="10" width="{w-20}" height="44" rx="10" fill="{A}" fill-opacity=".15"/>'
    s+=f'<text x="34" y="38" font-size="16" letter-spacing="4" class="k" filter="url(#glow)">[ SYSTEM ]</text><text x="{w-34}" y="38" text-anchor="end" font-size="13" letter-spacing="3" class="m">PLAYER STATUS</text>'
    # left info
    rows=[("NAME",NAME.title()),("COUNTRY",COUNTRY.title()),("JOB","Student & Full Stack Dev"),("TITLE",TITLE),("PASSION",PASSION)]
    y=100
    s+=f'<text x="40" y="{y}" font-size="46" font-weight="900" fill="url(#tx)" filter="url(#glow)">LV. {LEVEL}</text>'
    y=140
    for k,v in rows:
        s+=f'<text x="40" y="{y}" font-size="12" letter-spacing="2" class="m">{k}</text><text x="150" y="{y}" font-size="14" class="w">{e(v)}</text>'
        y+=30
    # vitals
    s+=bar(40,320,360,HP,"HP",0.3,"url(#bar)")
    s+=bar(40,364,360,MP,"MP",0.5,"url(#bar)")
    s+=bar(40,408,360,EXP,"EXP",0.7,"url(#bar)")
    s+=f'<line x1="440" y1="76" x2="440" y2="{h-30}" stroke="{A}" stroke-opacity=".3"/>'
    # stats
    s+=f'<text x="470" y="92" font-size="13" letter-spacing="3" class="k">ABILITIES</text>'
    y=130
    for i,(n,v) in enumerate(STATS):
        s+=bar(470,y,390,v,n,0.3+i*0.15); y+=54
    s+=corners(w,h,18)+'</svg>'
    return s

# ---------------- QUEST ----------------
def quest():
    w,h=900,520
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{defs(w,h)}'
    s+=f'<rect width="{w}" height="{h}" rx="14" fill="url(#bg)"/><rect width="{w}" height="{h}" rx="14" fill="url(#grid)"/>'
    s+=f'<rect x="10" y="10" width="{w-20}" height="44" rx="10" fill="{A}" fill-opacity=".15"/>'
    s+=f'<text x="34" y="38" font-size="16" letter-spacing="4" class="k" filter="url(#glow)">[ QUEST LOG ]</text><text x="{w-34}" y="38" text-anchor="end" font-size="13" letter-spacing="3" class="m">STATUS: IN PROGRESS</text>'
    # main quest
    s+=f'<rect x="34" y="78" width="{w-68}" height="70" rx="8" fill="{A}" fill-opacity=".1" stroke="{A}" stroke-opacity=".6"/>'
    s+=f'<text x="54" y="104" font-size="12" letter-spacing="3" class="m">MAIN QUEST</text>'
    s+=f'<text x="54" y="132" font-size="22" font-weight="800" fill="url(#tx)" filter="url(#glow)">⚔  {e(MAIN_QUEST)}</text>'
    s+=f'<text x="{w-54}" y="132" text-anchor="end" font-size="13" class="k">REWARD: ∞ EXP</text>'
    # training
    s+=f'<text x="40" y="188" font-size="13" letter-spacing="3" class="k">CURRENT TRAINING</text>'
    y=222
    for i,(n,v) in enumerate(TRAINING):
        s+=bar(40,y,390,v,n.upper(),0.3+i*0.2); y+=52
    # side quests
    s+=f'<line x1="470" y1="170" x2="470" y2="{h-30}" stroke="{A}" stroke-opacity=".3"/>'
    s+=f'<text x="500" y="188" font-size="13" letter-spacing="3" class="k">SIDE QUESTS</text>'
    y=222
    for i,q in enumerate(QUESTS):
        s+=f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur=".5s" begin="{0.4+i*0.35}s" fill="freeze"/>'
        s+=f'<rect x="500" y="{y-14}" width="14" height="14" rx="3" fill="none" stroke="{A}"/><path d="M503 {y-7}l3 3 6-8" fill="none" stroke="{C}" stroke-width="2"/>'
        s+=f'<text x="528" y="{y-2}" font-size="14" class="w">{e(q)}</text></g>'
        y+=44
    s+=f'<text x="{w//2}" y="{h-26}" text-anchor="middle" font-size="12" letter-spacing="4" class="m">HE WHO NEVER STOPS LEVELING UP.</text>'
    s+=corners(w,h,18)+'</svg>'
    return s

# ---------------- FOOTER ----------------
def footer():
    w,h=900,120
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{defs(w,h)}'
    s+=f'<rect width="{w}" height="{h}" rx="14" fill="url(#bg)"/><ellipse cx="450" cy="60" rx="300" ry="60" fill="url(#gl)"><animate attributeName="opacity" values=".4;1;.4" dur="3s" repeatCount="indefinite"/></ellipse>'
    s+=f'<text x="450" y="70" text-anchor="middle" font-size="40" font-weight="900" letter-spacing="14" fill="url(#tx)" filter="url(#glow)">ARISE<animate attributeName="opacity" values="1;.6;1" dur="2.4s" repeatCount="indefinite"/></text>'
    s+=f'<text x="450" y="98" text-anchor="middle" font-size="12" letter-spacing="5" class="m">THANKS FOR VISITING · {e(NAME)}</text></svg>'
    return s

for n,f in [("header",header),("status",status),("quest",quest),("footer",footer)]:
    open(f"{n}.svg","w",encoding="utf-8").write(f())
print("ok", sys.argv[1] if len(sys.argv)>1 else "shadow")
