
<!DOCTYPE html>
<html>
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Noto+Sans+JP:wght@300;400;700&family=Orbitron:wght@400;700;900&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: #050a12;
    font-family: 'Noto Sans JP', sans-serif;
    color: #e8e0d0;
    overflow-x: hidden;
    min-height: 100vh;
  }

  .stars {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0;
    background: radial-gradient(ellipse at 20% 30%, #0d1a2e 0%, #050a12 60%);
  }

  .star {
    position: absolute; width: 2px; height: 2px; background: white; border-radius: 50%;
    animation: twinkle 3s infinite alternate;
  }

  @keyframes twinkle { 0%{opacity:0.2;} 100%{opacity:1;} }

  .container { max-width: 900px; margin: 0 auto; padding: 0 20px; position: relative; z-index: 2; }

  /* HERO */
  .hero {
    padding: 60px 0 40px;
    text-align: center;
    position: relative;
  }

  .clan-emblem {
    width: 110px; height: 110px; margin: 0 auto 24px;
    position: relative;
  }

  .clan-emblem svg { width: 100%; height: 100%; }

  @keyframes spin-slow { from{transform:rotate(0deg);} to{transform:rotate(360deg);} }
  @keyframes pulse-glow { 0%,100%{filter:drop-shadow(0 0 8px #ff6b00) drop-shadow(0 0 20px #ff4500aa);} 50%{filter:drop-shadow(0 0 16px #ff6b00) drop-shadow(0 0 40px #ff4500);} }

  .emblem-outer { animation: spin-slow 20s linear infinite; }
  .emblem-core { animation: pulse-glow 2.5s ease-in-out infinite; }

  .hero-name {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(2.2rem, 6vw, 3.8rem);
    font-weight: 900;
    letter-spacing: 0.12em;
    background: linear-gradient(135deg, #ff6b00 0%, #ffaa00 40%, #ff3300 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 30px #ff6b0066);
    margin-bottom: 8px;
  }

  .hero-kanji {
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 1rem; font-weight: 300;
    color: #7a90b0; letter-spacing: 0.3em;
    margin-bottom: 16px;
  }

  .hero-subtitle {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.75rem; font-weight: 400;
    color: #8899bb; letter-spacing: 0.25em; text-transform: uppercase;
    margin-bottom: 32px;
  }

  .hero-divider {
    width: 300px; height: 1px; margin: 0 auto 32px;
    background: linear-gradient(90deg, transparent, #ff6b00, #9933ff, transparent);
    position: relative;
  }

  .hero-divider::after {
    content: '忍'; position: absolute; top: -12px; left: 50%; transform: translateX(-50%);
    font-size: 1.1rem; color: #ff6b00; background: #050a12; padding: 0 8px;
  }

  /* BIO CARDS */
  .bio-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px; margin-bottom: 40px;
  }

  .bio-card {
    background: linear-gradient(135deg, #0d1520 0%, #111a28 100%);
    border: 1px solid #1e2d44;
    border-radius: 10px; padding: 16px;
    position: relative; overflow: hidden;
    transition: transform 0.3s, border-color 0.3s;
  }

  .bio-card:hover { transform: translateY(-3px); border-color: #ff6b0066; }

  .bio-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, transparent, #ff6b00, transparent);
    opacity: 0;  transition: opacity 0.3s;
  }
  .bio-card:hover::before { opacity: 1; }

  .bio-icon { font-size: 1.4rem; margin-bottom: 8px; }
  .bio-label { font-size: 0.65rem; color: #7a90b0; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 4px; }
  .bio-value { font-size: 0.85rem; color: #e0d8cc; font-weight: 400; }

  /* SECTION HEADERS */
  .section-header {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 20px; margin-top: 40px;
  }

  .section-line { flex: 1; height: 1px; background: linear-gradient(90deg, #ff6b0033, transparent); }
  .section-line.right { background: linear-gradient(90deg, transparent, #ff6b0033); }

  .section-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.7rem; font-weight: 700; letter-spacing: 0.3em;
    color: #ff8833; text-transform: uppercase;
  }

  .section-kanji { font-size: 0.8rem; color: #3d4f6a; }

  /* JUTSU / TECH STACK */
  .jutsu-grid {
    display: flex; flex-wrap: wrap; gap: 8px; justify-content: center;
    margin-bottom: 8px;
  }

  .jutsu-badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 7px 14px; border-radius: 6px;
    font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em;
    border: 1px solid transparent;
    transition: all 0.3s; cursor: default;
    position: relative; overflow: hidden;
  }

  .jutsu-badge::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 60%);
  }

  .jutsu-badge:hover { transform: scale(1.05); }

  .badge-js    { background: #1a1600; border-color: #f0db4f44; color: #f0db4f; }
  .badge-bs    { background: #130d1f; border-color: #7952b344; color: #b07df5; }
  .badge-tw    { background: #001a1a; border-color: #38b2ac44; color: #5fd7d3; }
  .badge-java  { background: #1a0a00; border-color: #f89820aa; color: #f89820; }
  .badge-php   { background: #100e1a; border-color: #8892bf88; color: #a0aad3; }
  .badge-lar   { background: #1a0505; border-color: #ff2d2088; color: #ff6b6b; }
  .badge-mysql { background: #00070f; border-color: #00aaff55; color: #44bbff; }

  .badge-dot {
    width: 5px; height: 5px; border-radius: 50%;
    background: currentColor; opacity: 0.7;
    animation: badge-pulse 2s infinite;
  }

  @keyframes badge-pulse { 0%,100%{opacity:0.3;} 50%{opacity:1;} }

  /* NARUTO vs SASUKE BANNER */
  .rivals-banner {
    display: grid; grid-template-columns: 1fr auto 1fr;
    gap: 0; margin: 40px 0 32px; align-items: center;
  }

  .rival-card {
    padding: 24px 20px; border-radius: 12px;
    position: relative; overflow: hidden;
  }

  .rival-naruto {
    background: linear-gradient(135deg, #1a0d00 0%, #0d0a00 100%);
    border: 1px solid #ff6b0033;
    border-right: none; border-radius: 12px 0 0 12px;
    text-align: left;
  }

  .rival-sasuke {
    background: linear-gradient(135deg, #0d0010 0%, #060010 100%);
    border: 1px solid #9933ff33;
    border-left: none; border-radius: 0 12px 12px 0;
    text-align: right;
  }

  .rival-vs {
    background: #0d0a12; border: 1px solid #2a2040;
    padding: 16px 10px; text-align: center;
    display: flex; flex-direction: column; align-items: center; gap: 4px;
  }

  .vs-text {
    font-family: 'Orbitron', sans-serif; font-size: 1.4rem; font-weight: 900;
    background: linear-gradient(180deg, #ff6b00, #9933ff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px #9933ff66);
  }

  .rival-name {
    font-family: 'Orbitron', sans-serif; font-size: 0.85rem; font-weight: 700;
    letter-spacing: 0.15em; margin-bottom: 4px;
  }

  .rival-naruto .rival-name { color: #ff8833; }
  .rival-sasuke .rival-name { color: #bb77ff; }

  .rival-quote {
    font-size: 0.68rem; color: #7a90b0; font-style: italic; line-height: 1.5;
  }

  .rival-kanji {
    font-size: 2.5rem; color: #ffffff08; position: absolute;
    font-weight: 900;
  }

  .rival-naruto .rival-kanji { bottom: 8px; right: 12px; }
  .rival-sasuke .rival-kanji { bottom: 8px; left: 12px; }

  /* STATS SECTION */
  .stats-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px; margin-bottom: 24px;
  }

  .stat-card {
    background: #0a1018; border: 1px solid #1a2535;
    border-radius: 12px; overflow: hidden;
  }

  .stat-card-header {
    padding: 12px 16px;
    background: linear-gradient(90deg, #0d1520, #111a28);
    border-bottom: 1px solid #1a2535;
    font-family: 'Orbitron', sans-serif; font-size: 0.6rem;
    letter-spacing: 0.2em; color: #ff8833; text-transform: uppercase;
  }

  .stat-card-body { padding: 16px; }

  .stat-img {
    width: 100%; border-radius: 6px; display: block;
    filter: saturate(1.1) brightness(0.95);
    transition: filter 0.3s;
  }

  .stat-img:hover { filter: saturate(1.3) brightness(1.05); }

  /* TROPHIES */
  .trophy-wrap {
    background: #0a1018; border: 1px solid #1a2535; border-radius: 12px;
    overflow: hidden; margin-bottom: 16px;
  }

  .trophy-header {
    padding: 12px 16px;
    background: linear-gradient(90deg, #0d1520, #111a28);
    border-bottom: 1px solid #1a2535;
    font-family: 'Orbitron', sans-serif; font-size: 0.6rem;
    letter-spacing: 0.2em; color: #ffaa00;
  }

  .trophy-body { padding: 16px; text-align: center; }

  .trophy-img { width: 100%; max-width: 680px; border-radius: 6px; display: block; margin: 0 auto; }

  /* SCROLL BARS */
  .jutsu-bar-row { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
  .jutsu-bar-label { font-size: 0.7rem; color: #8899bb; width: 90px; flex-shrink: 0; }
  .jutsu-bar-track { flex: 1; height: 4px; background: #1a2535; border-radius: 2px; overflow: hidden; }
  .jutsu-bar-fill { height: 100%; border-radius: 2px; }
  .bar-js    { background: linear-gradient(90deg, #f0db4f, #e0c000); }
  .bar-java  { background: linear-gradient(90deg, #f89820, #e07000); }
  .bar-php   { background: linear-gradient(90deg, #8892bf, #5561a0); }
  .bar-lar   { background: linear-gradient(90deg, #ff2d20, #cc1010); }
  .bar-mysql { background: linear-gradient(90deg, #00aaff, #0077cc); }
  .jutsu-bar-pct { font-size: 0.65rem; color: #ff8833; width: 30px; text-align: right; }

  /* QUOTE */
  .quote-card {
    background: linear-gradient(135deg, #0d1520, #0a1018);
    border: 1px solid #1e2d44; border-left: 3px solid #ff6b00;
    border-radius: 0 10px 10px 0; padding: 20px 24px; margin: 24px 0;
    position: relative;
  }

  .quote-text {
    font-size: 0.9rem; color: #c8c0b0; line-height: 1.8; font-style: italic;
  }

  .quote-text span { color: #ff8833; font-style: normal; font-weight: 700; }

  .quote-attr { font-size: 0.65rem; color: #7a90b0; margin-top: 10px; letter-spacing: 0.1em; }

  /* FOOTER */
  .footer {
    text-align: center; padding: 40px 0 30px;
    border-top: 1px solid #1a2535; margin-top: 40px;
  }

  .footer-kanji {
    font-size: 2rem; color: #1e2d44; margin-bottom: 8px;
  }

  .footer-text {
    font-size: 0.65rem; color: #3d4f6a; letter-spacing: 0.2em;
  }

  /* SHARINGAN SPINNER */
  .sharingan-wrap { display: flex; justify-content: center; margin: 8px 0 24px; }

  @keyframes eye-spin { from{transform:rotate(0);} to{transform:rotate(360deg);} }
  @keyframes eye-glow { 0%,100%{filter:drop-shadow(0 0 4px #cc0000aa);} 50%{filter:drop-shadow(0 0 12px #cc0000);} }

  .sharingan-svg { animation: eye-glow 2s ease-in-out infinite; }
  .sharingan-inner { animation: eye-spin 4s linear infinite; transform-origin: 50px 50px; }

</style>

<div class="stars" id="stars-bg"></div>

<div class="container">

  <!-- HERO -->
  <div class="hero">
    <div class="clan-emblem">
      <svg viewBox="0 0 100 100" class="emblem-core">
        <g class="emblem-outer">
          <polygon points="50,5 61,35 95,35 68,57 79,91 50,70 21,91 32,57 5,35 39,35" fill="none" stroke="#ff6b00" stroke-width="1.5" opacity="0.6"/>
        </g>
        <circle cx="50" cy="50" r="22" fill="none" stroke="#ff6b00" stroke-width="1"/>
        <circle cx="50" cy="50" r="14" fill="none" stroke="#ffaa00" stroke-width="0.8" opacity="0.7"/>
        <text x="50" y="57" text-anchor="middle" font-family="Noto Sans JP,sans-serif" font-size="20" font-weight="700" fill="#ff8833">忍</text>
        <circle cx="50" cy="50" r="30" fill="none" stroke="#ff6b00" stroke-width="0.5" stroke-dasharray="3 4" opacity="0.4"/>
      </svg>
    </div>

    <div class="hero-name">LUY DEVBAIC</div>
    <div class="hero-kanji">ルイ・デブバイク &nbsp;|&nbsp; カンボジア忍者</div>
    <div class="hero-subtitle">Aspiring Developer · Cambodia · Web & Software Engineer</div>

    <div class="hero-divider"></div>

    <div class="bio-grid">
      <div class="bio-card">
        <div class="bio-icon">🔭</div>
        <div class="bio-label">Mission</div>
        <div class="bio-value">Building Web & Software Apps</div>
      </div>
      <div class="bio-card">
        <div class="bio-icon">🌱</div>
        <div class="bio-label">Training Arc</div>
        <div class="bio-value">Microservices · Docker · Cloud</div>
      </div>
      <div class="bio-card">
        <div class="bio-icon">🤝</div>
        <div class="bio-label">Alliance</div>
        <div class="bio-value">Open to Collaboration</div>
      </div>
      <div class="bio-card">
        <div class="bio-icon">⚡️</div>
        <div class="bio-label">Nindo</div>
        <div class="bio-value">Ideas → Real Applications</div>
      </div>
    </div>
  </div>

  <!-- RIVALS BANNER -->
  <div class="rivals-banner">
    <div class="rival-card rival-naruto">
      <div class="rival-name">NARUTO PATH</div>
      <div class="rival-quote">"I never go back on my word — that's my nindo, my ninja way."</div>
      <div class="rival-kanji">九</div>
    </div>
    <div class="rival-vs">
      <div style="font-size:0.55rem;color:#3d4f6a;letter-spacing:0.15em;">CHOOSE YOUR</div>
      <div class="vs-text">VS</div>
      <div style="font-size:0.55rem;color:#3d4f6a;letter-spacing:0.15em;">PATH</div>
    </div>
    <div class="rival-card rival-sasuke">
      <div class="rival-name">SASUKE PATH</div>
      <div class="rival-quote">"I am an avenger. I have only one goal — mastery."</div>
      <div class="rival-kanji">写</div>
    </div>
  </div>

  <!-- JUTSU / TECH STACK -->
  <div class="section-header">
    <div class="section-line"></div>
    <span class="section-kanji">術</span>
    <span class="section-title">Jutsu · Tech Stack</span>
    <span class="section-kanji">式</span>
    <div class="section-line right"></div>
  </div>

  <div class="jutsu-grid">
    <span class="jutsu-badge badge-js"><span class="badge-dot"></span>JavaScript</span>
    <span class="jutsu-badge badge-bs"><span class="badge-dot"></span>Bootstrap</span>
    <span class="jutsu-badge badge-tw"><span class="badge-dot"></span>Tailwind CSS</span>
    <span class="jutsu-badge badge-java"><span class="badge-dot"></span>Java</span>
    <span class="jutsu-badge badge-php"><span class="badge-dot"></span>PHP</span>
    <span class="jutsu-badge badge-lar"><span class="badge-dot"></span>Laravel</span>
    <span class="jutsu-badge badge-mysql"><span class="badge-dot"></span>MySQL</span>
  </div>

  <div style="background:#0a1018;border:1px solid #1a2535;border-radius:10px;padding:20px 24px;margin-top:16px;">
    <div class="jutsu-bar-row"><span class="jutsu-bar-label">JavaScript</span><div class="jutsu-bar-track"><div class="jutsu-bar-fill bar-js" style="width:82%"></div></div><span class="jutsu-bar-pct">82%</span></div>
    <div class="jutsu-bar-row"><span class="jutsu-bar-label">Java</span><div class="jutsu-bar-track"><div class="jutsu-bar-fill bar-java" style="width:70%"></div></div><span class="jutsu-bar-pct">70%</span></div>
    <div class="jutsu-bar-row"><span class="jutsu-bar-label">PHP</span><div class="jutsu-bar-track"><div class="jutsu-bar-fill bar-php" style="width:65%"></div></div><span class="jutsu-bar-pct">65%</span></div>
    <div class="jutsu-bar-row"><span class="jutsu-bar-label">Laravel</span><div class="jutsu-bar-track"><div class="jutsu-bar-fill bar-lar" style="width:60%"></div></div><span class="jutsu-bar-pct">60%</span></div>
    <div class="jutsu-bar-row"><span class="jutsu-bar-label">MySQL</span><div class="jutsu-bar-track"><div class="jutsu-bar-fill bar-mysql" style="width:72%"></div></div><span class="jutsu-bar-pct">72%</span></div>
  </div>

  <!-- SHARINGAN -->
  <div class="section-header" style="margin-top:40px;">
    <div class="section-line"></div>
    <span class="section-kanji">写</span>
    <span class="section-title">Sharingan · GitHub Stats</span>
    <span class="section-kanji">輪</span>
    <div class="section-line right"></div>
  </div>

  <div class="sharingan-wrap">
    <svg class="sharingan-svg" width="60" height="60" viewBox="0 0 100 100">
      <circle cx="50" cy="50" r="48" fill="#1a0000" stroke="#cc0000" stroke-width="1.5"/>
      <circle cx="50" cy="50" r="30" fill="#cc0000" opacity="0.15"/>
      <circle cx="50" cy="50" r="20" fill="#cc1100"/>
      <g class="sharingan-inner">
        <path d="M50 30 Q60 50 50 50 Q40 50 50 30Z" fill="#1a0000"/>
        <path d="M50 70 Q60 50 50 50 Q40 50 50 70Z" fill="#1a0000"/>
        <path d="M30 40 Q50 45 50 50 Q50 55 30 60Z" fill="#1a0000"/>
      </g>
      <circle cx="50" cy="50" r="8" fill="#0a0000"/>
      <circle cx="46" cy="47" r="2.5" fill="#ffffff33"/>
    </svg>
  </div>

  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-card-header">⚔ Overall Contributions</div>
      <div class="stat-card-body">
        <img class="stat-img" src="https://github-readme-stats.vercel.app/api?username=Devbaic&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&bg_color=0a1018&title_color=ff8833&text_color=c8c0b0&icon_color=ff6b00" alt="GitHub Stats" loading="lazy">
      </div>
    </div>
    <div class="stat-card">
      <div class="stat-card-header">🔥 Chakra Streak</div>
      <div class="stat-card-body">
        <img class="stat-img" src="https://github-readme-streak-stats.herokuapp.com/?user=Devbaic&theme=tokyonight&hide_border=true&background=0a1018&fire=ff6b00&ring=ff8833&currStreakLabel=ffaa00&sideLabels=c8c0b0&currStreakNum=ff6b00&sideNums=e0d8cc&dates=7a90b0" alt="Streak" loading="lazy">
      </div>
    </div>
  </div>

  <div class="stat-card" style="margin-bottom:16px;">
    <div class="stat-card-header">🌀 Kekkei Genkai · Top Languages</div>
    <div class="stat-card-body">
      <img class="stat-img" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Devbaic&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true&layout=compact&bg_color=0a1018&title_color=ff8833&text_color=c8c0b0" alt="Top Languages" loading="lazy">
    </div>
  </div>

  <!-- TROPHIES -->
  <div class="trophy-wrap">
    <div class="trophy-header">🏆 Kage-Level Trophies</div>
    <div class="trophy-body">
      <img class="trophy-img" src="https://github-profile-trophy.vercel.app/?username=Devbaic&theme=tokyonight&no-frame=true&margin-w=8" alt="Trophies" loading="lazy">
    </div>
  </div>

  <!-- DEV QUOTE -->
  <div class="section-header">
    <div class="section-line"></div>
    <span class="section-kanji">言</span>
    <span class="section-title">Sensei's Wisdom</span>
    <span class="section-kanji">葉</span>
    <div class="section-line right"></div>
  </div>

  <div class="quote-card">
    <div class="quote-text">"The <span>code</span> is like chakra — you don't just learn it, you breathe it. Every commit is a step on the path of the shinobi developer."</div>
    <div class="quote-attr">— Luy's Ninja Dev Way · 忍者開発者の道</div>
  </div>

  <div style="background:#0a1018;border:1px solid #1a2535;border-radius:10px;overflow:hidden;margin-bottom:24px;">
    <div style="padding:10px 16px;border-bottom:1px solid #1a2535;font-family:'Orbitron',sans-serif;font-size:0.6rem;letter-spacing:0.2em;color:#9933ff;">✍ Random Dev Quote</div>
    <div style="padding:12px;">
      <img style="width:100%;border-radius:6px;" src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" alt="Dev Quote" loading="lazy">
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <div class="footer-kanji">忍道</div>
    <div style="display:flex;justify-content:center;gap:6px;margin:8px 0 12px;flex-wrap:wrap;">
      <span style="font-size:0.65rem;padding:3px 10px;border:1px solid #ff6b0033;border-radius:4px;color:#ff8833;">🇰🇭 Cambodia</span>
      <span style="font-size:0.65rem;padding:3px 10px;border:1px solid #9933ff33;border-radius:4px;color:#bb77ff;">💻 Web Dev</span>
      <span style="font-size:0.65rem;padding:3px 10px;border:1px solid #ffaa0033;border-radius:4px;color:#ffaa00;">☁ Cloud Learner</span>
    </div>
    <div class="footer-text">DEVBAIC · LUY · 忍者開発者 · CAMBODIA · 2025</div>
  </div>

</div>

<script>
const bg = document.getElementById('stars-bg');
for(let i=0;i<80;i++){
  const s = document.createElement('div');
  s.className='star';
  s.style.cssText=`left:${Math.random()*100}%;top:${Math.random()*100}%;animation-delay:${Math.random()*3}s;animation-duration:${2+Math.random()*3}s;opacity:${Math.random()*0.6+0.1};width:${Math.random()<0.2?3:2}px;height:${Math.random()<0.2?3:2}px;`;
  bg.appendChild(s);
}
</script>
