"""Loader Gallery — 10 hand-picked animated loaders, pure CSS/SVG."""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Loader Gallery", page_icon="🌀", layout="wide")

st.markdown(
    """
    <style>
      .block-container {padding-top: 2.2rem; max-width: 1200px;}
      .hero h1 {font-size: 2.4rem; margin-bottom: .2rem;
        background: linear-gradient(90deg,#8b7cff,#4fd1ff 50%,#ff7ab6);
        -webkit-background-clip: text; background-clip: text; color: transparent;}
      .hero p {color:#6b7086; margin-top:0;}
      .card-title {font-weight:600; font-size:1.02rem; margin:-.4rem 0 0 .2rem;}
      .card-sub {color:#6b7086; font-size:.85rem; margin:0 0 1.4rem .2rem;}
    </style>
    <div class="hero">
      <h1>Loader Gallery</h1>
      <p>20 animated loaders: 10 hand-built in CSS / SVG, plus the 10 best of 40 reviewed on LottieFiles.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

BASE = """
<style>
  html,body{margin:0;height:100%;background:transparent;}
  .stage{height:220px;border-radius:20px;display:flex;align-items:center;justify-content:center;
    background:radial-gradient(120% 120% at 50% 0%, #ffffff 0%, #f7f7fc 60%, #f1f2f9 100%);
    border:1px solid #e6e7f0;box-shadow:0 1px 2px rgba(20,20,50,.04);
    overflow:hidden;position:relative;font-family:system-ui,-apple-system,Segoe UI,sans-serif;}
  @media (prefers-reduced-motion: reduce){ *{animation-duration:6s !important;} }
</style>
"""

LOADERS = [
    # 1 — Aurora ring: conic gradient ring with a soft glow
    ("Aurora Ring", "Conic-gradient ring with a blurred glow halo", """
<style>
.aur{width:84px;height:84px;border-radius:50%;position:relative;
  background:conic-gradient(from 0deg,#8b7cff,#4fd1ff,#5effc1,#ff7ab6,#8b7cff);
  -webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 9px),#000 calc(100% - 8px));
          mask:radial-gradient(farthest-side,transparent calc(100% - 9px),#000 calc(100% - 8px));
  animation:spin 1.1s linear infinite;}
.aur-glow{position:absolute;width:84px;height:84px;border-radius:50%;filter:blur(14px);opacity:.6;
  -webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 12px),#000 calc(100% - 10px));
          mask:radial-gradient(farthest-side,transparent calc(100% - 12px),#000 calc(100% - 10px));
  background:conic-gradient(from 0deg,#8b7cff,#4fd1ff,#5effc1,#ff7ab6,#8b7cff);animation:spin 1.1s linear infinite;}
@keyframes spin{to{transform:rotate(1turn)}}
</style>
<div class="stage"><div class="aur-glow"></div><div class="aur"></div></div>
"""),
    # 2 — Gooey blobs: SVG goo filter merges orbiting dots
    ("Gooey Blobs", "SVG goo filter — dots melt into each other", """
<svg width="0" height="0" style="position:absolute"><defs><filter id="goo">
 <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="b"/>
 <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -9"/>
</filter></defs></svg>
<style>
.goo{width:110px;height:110px;position:relative;filter:url(#goo);animation:spin 3s linear infinite;}
.goo span{position:absolute;top:50%;left:50%;width:30px;height:30px;margin:-15px;border-radius:50%;
  background:linear-gradient(135deg,#ff7ab6,#8b7cff);animation:g 1.6s ease-in-out infinite;}
.goo span:nth-child(2){animation-delay:-.4s;background:linear-gradient(135deg,#8b7cff,#4fd1ff)}
.goo span:nth-child(3){animation-delay:-.8s;background:linear-gradient(135deg,#4fd1ff,#5effc1)}
.goo span:nth-child(4){animation-delay:-1.2s}
.goo span:nth-child(1){--a:0deg}.goo span:nth-child(2){--a:90deg}.goo span:nth-child(3){--a:180deg}.goo span:nth-child(4){--a:270deg}
@keyframes g{0%,100%{transform:rotate(var(--a)) translateX(0)}50%{transform:rotate(var(--a)) translateX(34px)}}
@keyframes spin{to{transform:rotate(1turn)}}
</style>
<div class="stage"><div class="goo"><span></span><span></span><span></span><span></span></div></div>
"""),
    # 3 — Orbit: tilted planetary system
    ("Orbit", "Three moons on tilted elliptical orbits", """
<style>
.sys{width:120px;height:120px;position:relative;transform:rotateX(62deg);transform-style:preserve-3d;}
.sun{position:absolute;inset:44px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff3c4,#ffb44f 55%,#ff7a45);
  box-shadow:0 0 24px #ffb44f88;transform:rotateX(-62deg);}
.ring{position:absolute;border-radius:50%;border:1px solid rgba(30,30,80,.12);animation:spin linear infinite;}
.ring::after{content:"";position:absolute;top:-6px;left:50%;width:12px;height:12px;margin-left:-6px;border-radius:50%;
  background:var(--c);box-shadow:0 0 12px var(--c);}
.r1{inset:26px;--c:#4fd1ff;animation-duration:1.4s}
.r2{inset:10px;--c:#ff7ab6;animation-duration:2.3s}
.r3{inset:-8px;--c:#5effc1;animation-duration:3.4s}
@keyframes spin{to{transform:rotate(1turn)}}
</style>
<div class="stage" style="perspective:500px"><div class="sys"><div class="ring r3"></div><div class="ring r2"></div><div class="ring r1"></div><div class="sun"></div></div></div>
"""),
    # 4 — DNA helix: phase-shifted dot pairs
    ("DNA Helix", "Phase-shifted dot pairs twist like a strand", """
<style>
.dna{display:flex;gap:9px;align-items:center;height:80px}
.dna i{position:relative;width:8px;height:80px}
.dna i::before,.dna i::after{content:"";position:absolute;left:0;width:8px;height:8px;border-radius:50%;
  animation:up 1.6s ease-in-out infinite;animation-delay:calc(var(--i)*-.12s)}
.dna i::before{background:#4fd1ff;box-shadow:0 0 10px #4fd1ff}
.dna i::after{background:#ff7ab6;box-shadow:0 0 10px #ff7ab6;animation-name:down}
@keyframes up{0%,100%{top:0;transform:scale(1)}25%{transform:scale(.5);opacity:.5}50%{top:72px;transform:scale(1)}75%{transform:scale(1.4)}}
@keyframes down{0%,100%{top:72px;transform:scale(1)}25%{transform:scale(1.4)}50%{top:0;transform:scale(1)}75%{transform:scale(.5);opacity:.5}}
</style>
<div class="stage"><div class="dna">
""" + "".join(f'<i style="--i:{n}"></i>' for n in range(12)) + "</div></div>"),
    # 5 — Equalizer wave bars
    ("Equalizer", "Gradient bars ripple like an audio wave", """
<style>
.eq{display:flex;gap:6px;align-items:center;height:80px}
.eq b{width:7px;height:100%;border-radius:6px;background:linear-gradient(180deg,#5effc1,#4fd1ff 50%,#8b7cff);
  transform-origin:center;animation:eq 1.1s ease-in-out infinite;animation-delay:calc(var(--i)*-.09s)}
@keyframes eq{0%,100%{transform:scaleY(.18);opacity:.6}50%{transform:scaleY(1);opacity:1}}
</style>
<div class="stage"><div class="eq">
""" + "".join(f'<b style="--i:{n}"></b>' for n in range(11)) + "</div></div>"),
    # 6 — Morphing shape
    ("Morph", "Square ↔ blob ↔ circle with shifting hue", """
<style>
.mo{width:74px;height:74px;background:linear-gradient(135deg,#8b7cff,#ff7ab6);
  box-shadow:0 10px 40px -6px #ff7ab688;animation:mo 3.2s cubic-bezier(.6,0,.4,1) infinite;}
@keyframes mo{
 0%{border-radius:18%;transform:rotate(0) scale(1);filter:hue-rotate(0)}
 25%{border-radius:60% 40% 30% 70%/60% 30% 70% 40%;transform:rotate(90deg) scale(.9)}
 50%{border-radius:50%;transform:rotate(180deg) scale(.75);filter:hue-rotate(110deg)}
 75%{border-radius:30% 70% 70% 30%/30% 30% 70% 70%;transform:rotate(270deg) scale(.9)}
 100%{border-radius:18%;transform:rotate(360deg) scale(1);filter:hue-rotate(0)}}
</style>
<div class="stage"><div class="mo"></div></div>
"""),
    # 7 — Ripple / sonar
    ("Ripple", "Calm sonar rings expanding from a core", """
<style>
.rp{position:relative;width:120px;height:120px;display:grid;place-items:center}
.rp span{position:absolute;inset:0;border-radius:50%;border:2px solid #4fd1ff;opacity:0;
  animation:rp 2.4s cubic-bezier(.2,.6,.3,1) infinite}
.rp span:nth-child(2){animation-delay:.8s;border-color:#8b7cff}
.rp span:nth-child(3){animation-delay:1.6s;border-color:#5effc1}
.rp em{width:18px;height:18px;border-radius:50%;background:linear-gradient(135deg,#8b7cff,#4fd1ff);box-shadow:0 0 14px #4fd1ff88;
  animation:beat 1.2s ease-in-out infinite}
@keyframes rp{0%{transform:scale(.15);opacity:1}100%{transform:scale(1);opacity:0}}
@keyframes beat{50%{transform:scale(.75)}}
</style>
<div class="stage"><div class="rp"><span></span><span></span><span></span><em></em></div></div>
"""),
    # 8 — Infinity stroke
    ("Infinity", "A comet tracing a lemniscate path", """
<style>
.inf path{fill:none;stroke-linecap:round}
.inf .track{stroke:rgba(30,30,80,.07);stroke-width:7}
.inf .run{stroke:url(#ig);stroke-width:7;stroke-dasharray:60 240;animation:dash 1.8s linear infinite;
  filter:drop-shadow(0 0 6px #8b7cff)}
@keyframes dash{to{stroke-dashoffset:-300}}
</style>
<div class="stage"><svg class="inf" width="150" height="80" viewBox="0 0 150 80">
<defs><linearGradient id="ig" x1="0" x2="1"><stop offset="0" stop-color="#4fd1ff"/><stop offset=".5" stop-color="#8b7cff"/><stop offset="1" stop-color="#ff7ab6"/></linearGradient></defs>
<path pathLength="300" class="track" d="M75 40 C55 10,15 10,15 40 C15 70,55 70,75 40 C95 10,135 10,135 40 C135 70,95 70,75 40Z"/>
<path pathLength="300" class="run" d="M75 40 C55 10,15 10,15 40 C15 70,55 70,75 40 C95 10,135 10,135 40 C135 70,95 70,75 40Z"/>
</svg></div>
"""),
    # 9 — Newton's cradle
    ("Newton's Cradle", "Physics-y swing with eased momentum", """
<style>
.nc{display:flex;padding-top:10px}
.nc div{width:22px;height:80px;transform-origin:50% 0;position:relative}
.nc div::before{content:"";position:absolute;left:50%;top:0;width:1px;height:58px;background:rgba(30,30,80,.25)}
.nc div::after{content:"";position:absolute;left:0;bottom:0;width:22px;height:22px;border-radius:50%;
  background:radial-gradient(circle at 35% 30%,#fff,#bfb6ff 30%,#8b7cff 70%,#5a49d6);box-shadow:0 6px 14px -4px #8b7cffaa}
.nc div:first-child{animation:l 1.2s cubic-bezier(.45,0,.55,1) infinite}
.nc div:last-child{animation:r 1.2s cubic-bezier(.45,0,.55,1) infinite}
@keyframes l{0%,50%,100%{transform:rotate(0)}25%{transform:rotate(38deg)}}
@keyframes r{0%,50%,100%{transform:rotate(0)}75%{transform:rotate(-38deg)}}
</style>
<div class="stage"><div class="nc"><div></div><div></div><div></div><div></div><div></div></div></div>
"""),
    # 10 — Shimmer text + progress line
    ("Shimmer Text", "Light sweep across text with an indeterminate bar", """
<style>
.sh{display:flex;flex-direction:column;align-items:center;gap:16px}
.sh h3{margin:0;font-size:34px;font-weight:800;letter-spacing:.06em;
  background:linear-gradient(100deg,#c7c9da 20%,#8b7cff 40%,#ff7ab6 50%,#c7c9da 70%);background-size:250% 100%;
  -webkit-background-clip:text;background-clip:text;color:transparent;animation:sh 1.8s linear infinite}
.bar{width:170px;height:4px;border-radius:4px;background:rgba(30,30,80,.07);overflow:hidden;position:relative}
.bar::after{content:"";position:absolute;inset:0;width:40%;border-radius:4px;
  background:linear-gradient(90deg,#4fd1ff,#8b7cff,#ff7ab6);animation:bar 1.4s cubic-bezier(.65,0,.35,1) infinite}
@keyframes sh{from{background-position:150% 0}to{background-position:-100% 0}}
@keyframes bar{0%{transform:translateX(-100%)}100%{transform:translateX(250%)}}
</style>
<div class="stage"><div class="sh"><h3>LOADING</h3><div class="bar"></div></div></div>
"""),
]

def grid(items, render):
    for i in range(0, len(items), 2):
        cols = st.columns(2, gap="medium")
        for col, (idx, item) in zip(cols, enumerate(items[i : i + 2], start=i + 1)):
            with col:
                render(idx, item)


st.markdown("### CSS & SVG loaders")
st.caption("Pure CSS / SVG — no JavaScript, no images.")
cols_per_row = 2
for i in range(0, len(LOADERS), cols_per_row):
    cols = st.columns(cols_per_row, gap="medium")
    for col, (idx, (name, sub, html)) in zip(cols, enumerate(LOADERS[i : i + cols_per_row], start=i + 1)):
        with col:
            components.html(BASE + html, height=222)
            st.markdown(
                f'<div class="card-title">{idx:02d} · {name}</div><div class="card-sub">{sub}</div>',
                unsafe_allow_html=True,
            )


# ---------------------------------------------------------------- Lottie section
import json
from pathlib import Path

LOTTIE = json.loads((Path(__file__).parent / "static/lottie/index.json").read_text())

LOTTIE_TPL = BASE + """
<div class="stage"><div id="a" style="width:190px;height:190px"></div></div>
<script>
(async () => {
  const base = "/app/static/";
  if (!window.lottie) { eval(await (await fetch(base + "lottie.min.js")).text()); }
  const data = await (await fetch(base + "lottie/__FILE__")).json();
  lottie.loadAnimation({container: document.getElementById("a"), renderer: "svg",
                        loop: true, autoplay: true, animationData: data});
})();
</script>
"""


def render_lottie(idx, m):
    components.html(LOTTIE_TPL.replace("__FILE__", m["file"]), height=222)
    st.markdown(
        f'<div class="card-title">{idx:02d} · {m["name"]}</div>'
        f'<div class="card-sub">{m["sub"]} · by <a href="{m["url"]}" target="_blank">{m["author"]}</a> on LottieFiles</div>',
        unsafe_allow_html=True,
    )


st.markdown("### Lottie loaders")
st.caption("The 10 best of 40 free loading animations reviewed on LottieFiles, played with lottie-web.")
grid(LOTTIE, render_lottie)

with st.expander("CSS research shortlist — the ~28 patterns considered"):
    st.markdown(
        """
**Picked (10):** Aurora conic ring · Gooey blobs · Orbit · DNA helix · Equalizer bars · Morphing blob ·
Ripple/sonar · Infinity path · Newton's cradle · Shimmer text + bar

**Considered, not picked:** classic border spinner · three bouncing dots · typing dots · pulsing dot ·
skeleton shimmer · Material circular · cube grid · folding cube · 3D rotating cube · flipping square ·
hourglass · radar sweep · liquid fill · heartbeat line · Olympic rings · solar eclipse · snake/worm ·
clock hands

Chosen for motion quality (eased, continuous, non-jarring), visual distinctiveness from each other,
a cohesive violet/cyan/pink/mint palette, and good legibility on a phone screen.
"""
    )
