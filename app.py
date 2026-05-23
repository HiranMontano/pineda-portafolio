import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import urlparse, parse_qs


def get_youtube_id(url: str) -> str | None:
    try:
        p = urlparse(url)
        host = (p.hostname or "").replace("www.", "")
        if host == "youtu.be":
            return p.path.lstrip("/").split("/")[0]
        if "youtube.com" in host:
            if p.path.startswith("/watch"):
                return parse_qs(p.query).get("v", [None])[0]
            if "/shorts/" in p.path:
                return p.path.split("/shorts/")[1].split("/")[0]
            if "/embed/" in p.path:
                return p.path.split("/embed/")[1].split("/")[0]
    except Exception:
        pass
    return None


VIDEOS = [
    {"url": "https://www.youtube.com/watch?v=YCxhXTU4NrE", "title": "Grabaciones de estudio", "sub": "Mr / LOS FAROS"},
    {"url": "https://youtube.com/shorts/r7QvKXb2bo4",       "title": "Arreglos",               "sub": "YouTube"},
    {"url": "https://www.youtube.com/shorts/7lq5X5ncoKE",   "title": "Live (Sevijazz 2025)",   "sub": "Latin jazz / Bass Impro"},
]
for v in VIDEOS:
    vid = get_youtube_id(v["url"])
    v["thumb"] = f"https://img.youtube.com/vi/{vid}/hqdefault.jpg" if vid else ""

st.set_page_config(
    page_title="Juan David Pineda — Músico & Productor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip every pixel of Streamlit chrome so the iframe fills the screen
st.markdown("""
<style>
#MainMenu,
header[data-testid="stHeader"],
footer,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
.stDeployButton,
section[data-testid="stSidebar"] { display: none !important; }

html, body, .stApp { margin: 0; padding: 0; overflow: hidden; background: #111014 !important; }
.block-container, section.main, section.main > div { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
iframe { border: none !important; display: block !important; }
</style>
""", unsafe_allow_html=True)

# ── Full standalone HTML (CSS/JS braces left literal – no f-string) ──────────
FULL_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Portafolio de músico, bajista, productor, beatmaker y arreglista." />
  <title>Juan David Pineda — Músico & Productor</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Bebas+Neue&family=Anton&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --red: #ec0d0d;
      --red-dark: #8f1018;
      --brick: #693947;
      --mauve: #8c5060;
      --ink: #17151a;
      --charcoal: #262229;
      --paper: #f0f0f6;
      --silver: #a89ca2;
      --line: rgba(240, 240, 246, 0.18);
      --shadow: rgba(0, 0, 0, 0.55);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    body {
      min-height: 100vh;
      background:
        radial-gradient(circle at 20% 5%, rgba(236, 13, 13, 0.20), transparent 28rem),
        radial-gradient(circle at 80% 20%, rgba(105, 57, 71, 0.35), transparent 36rem),
        linear-gradient(135deg, #111014 0%, #1e1a20 48%, #0c0b0e 100%);
      color: var(--paper);
      font-family: 'Space Mono', monospace;
      overflow-x: hidden;
    }

    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      background-image:
        linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px),
        url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.24'/%3E%3C/svg%3E");
      background-size: 46px 46px, 46px 46px, 260px 260px;
      mix-blend-mode: overlay;
      opacity: 0.7;
    }

    a { color: inherit; text-decoration: none; }
    img { display: block; max-width: 100%; }

    .page { position: relative; z-index: 1; }

    .topbar {
      position: sticky;
      top: 0;
      z-index: 20;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      padding: 1rem clamp(1rem, 4vw, 3rem);
      background: rgba(17, 16, 20, 0.82);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(236, 13, 13, 0.28);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: .75rem;
      font-family: 'Archivo Black', sans-serif;
      text-transform: uppercase;
      letter-spacing: -0.04em;
      font-size: clamp(1.1rem, 2.4vw, 1.85rem);
      line-height: 0.9;
    }
    .brand span { color: var(--red); text-shadow: 2px 2px 0 #000; }

    .navlinks {
      display: flex;
      gap: clamp(.5rem, 2vw, 1.5rem);
      flex-wrap: wrap;
      justify-content: flex-end;
      font-size: .72rem;
      text-transform: uppercase;
      letter-spacing: .12em;
    }
    .navlinks a {
      padding: .45rem .1rem;
      color: rgba(240,240,246,.76);
      border-bottom: 2px solid transparent;
      transition: .2s ease;
    }
    .navlinks a:hover { color: var(--paper); border-color: var(--red); }

    .section { padding: clamp(4rem, 9vw, 7.5rem) clamp(1rem, 4vw, 3rem); }

    .section-kicker {
      display: inline-block;
      margin-bottom: 1rem;
      color: var(--red);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .22em;
      font-size: .72rem;
    }

    .section-title {
      font-family: 'Archivo Black', sans-serif;
      text-transform: uppercase;
      font-size: clamp(2.2rem, 7vw, 6rem);
      line-height: .86;
      letter-spacing: -0.08em;
      max-width: 12ch;
      text-shadow: 4px 4px 0 #000;
    }
    .red-word { color: var(--red); }

    .button-row { display: flex; flex-wrap: wrap; gap: .85rem; margin-top: 1.75rem; }

    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 44px;
      padding: .85rem 1rem;
      border: 2px solid var(--paper);
      box-shadow: 5px 5px 0 #000;
      background: var(--red);
      color: var(--paper);
      font-family: 'Archivo Black', sans-serif;
      text-transform: uppercase;
      letter-spacing: .04em;
      transition: transform .18s ease, box-shadow .18s ease, background .18s ease;
    }
    .btn.secondary { background: transparent; color: var(--paper); }
    .btn:hover { transform: translate(3px, 3px); box-shadow: 2px 2px 0 #000; }

    /* ── BIO ── */
    #bio {
      min-height: calc(100vh - 68px);
      display: grid;
      grid-template-columns: minmax(0, 1.15fr) minmax(280px, .85fr);
      gap: clamp(2rem, 6vw, 5rem);
      align-items: center;
      border-bottom: 1px solid var(--line);
    }
    .bio-copy { max-width: 820px; position: relative; }

    .stamp {
      display: inline-flex;
      align-items: center;
      gap: .55rem;
      transform: rotate(-2deg);
      padding: .35rem .6rem;
      border: 2px solid var(--red);
      color: var(--red);
      font-size: .72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .18em;
      margin-bottom: 1.2rem;
      background: rgba(0,0,0,.22);
    }

    .bio-headline {
      font-family: 'Archivo Black', sans-serif;
      font-size: clamp(3rem, 10vw, 8.5rem);
      line-height: .78;
      letter-spacing: -0.09em;
      text-transform: uppercase;
      text-shadow: 6px 6px 0 #000;
    }
    .bio-headline .glitch {
      display: inline-block;
      font-family: 'Anton', 'Archivo Black', sans-serif;
      color: var(--red);
      letter-spacing: -0.04em;
      text-shadow: 5px 5px 0 #000;
      line-height: .82;
      transform: translateY(2px);
      -webkit-font-smoothing: antialiased;
      text-rendering: geometricPrecision;
    }

    .bio-text {
      margin-top: 1.6rem;
      max-width: 680px;
      font-size: clamp(1rem, 1.7vw, 1.25rem);
      line-height: 1.8;
      color: rgba(240,240,246,.82);
    }
    .bio-text strong { color: var(--paper); }

    .role-tags { display: flex; flex-wrap: wrap; gap: .65rem; margin-top: 1.3rem; }
    .tag {
      padding: .42rem .62rem;
      background: rgba(240,240,246,.08);
      border: 1px solid rgba(240,240,246,.18);
      color: rgba(240,240,246,.78);
      text-transform: uppercase;
      font-size: .72rem;
      letter-spacing: .12em;
    }

    .bio-card {
      position: relative;
      min-height: 520px;
      border: 2px solid var(--paper);
      background:
        linear-gradient(0deg, rgba(236,13,13,.25), rgba(0,0,0,.1)),
        linear-gradient(135deg, var(--brick), var(--charcoal));
      box-shadow: 18px 18px 0 #000;
      overflow: hidden;
      transform: rotate(1.2deg);
    }
    .bio-main-img {
      width: 100%; height: 100%;
      object-fit: cover; object-position: center;
      filter: contrast(1.08) saturate(0.95);
      transition: transform .35s ease, filter .35s ease;
    }
    .bio-card:hover .bio-main-img { transform: scale(1.04); filter: contrast(1.15) saturate(1.05); }

    .parental {
      position: absolute; right: 1rem; bottom: 1rem;
      padding: .35rem .45rem;
      border: 2px solid var(--paper);
      color: var(--paper); background: #000;
      font-family: Arial, sans-serif; font-weight: 900; font-size: .75rem;
      line-height: .85; text-align: center; text-transform: uppercase; max-width: 110px;
    }

    /* ── IMAGE GRID ── */
    .image-grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: .9rem;
      margin-top: 2.5rem;
    }
    .image-card {
      min-height: 260px;
      border: 2px solid rgba(240,240,246,.75);
      background: linear-gradient(135deg, rgba(236,13,13,.28), rgba(105,57,71,.5)), var(--charcoal);
      position: relative; overflow: hidden;
      box-shadow: 8px 8px 0 #000;
    }
    .image-card:nth-child(1) { grid-column: span 5; min-height: 460px; }
    .image-card:nth-child(2) { grid-column: span 4; min-height: 300px; }
    .image-card:nth-child(3) { grid-column: span 3; min-height: 300px; }
    .image-card:nth-child(4) { grid-column: span 7; min-height: 320px; }
    .image-card:nth-child(5) { grid-column: span 5; min-height: 320px; }
    .image-card::after {
      content: attr(data-label);
      position: absolute; left: .85rem; bottom: .85rem;
      background: var(--paper); color: #000;
      font-family: 'Archivo Black', sans-serif;
      font-size: clamp(1.2rem, 3vw, 2.5rem);
      text-transform: uppercase; line-height: .9;
      padding: .25rem .45rem;
      box-decoration-break: clone;
      -webkit-box-decoration-break: clone;
    }
    .portfolio-img {
      width: 100%; height: 100%;
      object-fit: cover; object-position: center;
      filter: contrast(1.08) saturate(0.9);
      transition: transform .35s ease, filter .35s ease;
    }
    .image-card:hover .portfolio-img { transform: scale(1.06); filter: contrast(1.15) saturate(1.05); }

    /* ── VIDEOS ── */
    .video-layout {
      display: grid;
      grid-template-columns: 1.4fr .9fr;
      gap: 1rem;
      margin-top: 2.5rem;
    }
    .video-card {
      position: relative; min-height: 280px;
      display: grid; place-items: center;
      border: 2px solid rgba(240,240,246,.8);
      background:
        linear-gradient(135deg, rgba(0,0,0,.55), rgba(236,13,13,.18)),
        repeating-linear-gradient(0deg, #1b1820 0 6px, #211d25 6px 12px);
      overflow: hidden; box-shadow: 8px 8px 0 #000;
      color: var(--paper); text-decoration: none;
    }
    .video-main { min-height: 600px; }
    .video-stack { display: grid; gap: 1rem; }

    .video-thumb {
      position: absolute; inset: 0;
      width: 100%; height: 100%; max-width: none;
      object-fit: cover; object-position: center; z-index: 0;
      filter: contrast(1.08) saturate(0.9) brightness(0.68);
      transition: transform .35s ease, filter .35s ease;
    }
    .video-card:hover .video-thumb { transform: scale(1.06); filter: contrast(1.15) saturate(1.05) brightness(0.82); }

    .video-card::after {
      content: "";
      position: absolute; inset: 0; z-index: 1;
      background: linear-gradient(to top, rgba(0,0,0,.92) 0%, rgba(0,0,0,.45) 45%, rgba(236,13,13,.14) 100%);
      pointer-events: none;
    }

    .play {
      width: 78px; height: 78px; border-radius: 50%;
      display: grid; place-items: center;
      border: 3px solid var(--paper);
      color: var(--paper); background: var(--red);
      box-shadow: 6px 6px 0 #000;
      font-family: 'Archivo Black', sans-serif;
      font-size: 1.7rem; padding-left: .2rem;
      position: relative; z-index: 2;
      transition: transform .2s ease;
    }
    .video-card:hover .play { transform: scale(1.08); }

    .video-caption {
      position: absolute; left: 1rem; right: 1rem; bottom: 1rem;
      display: flex; justify-content: space-between; gap: 1rem; align-items: end;
      border-top: 1px solid rgba(240,240,246,.25);
      padding-top: .8rem; z-index: 2;
    }
    .video-caption h3 {
      font-family: 'Archivo Black', sans-serif;
      text-transform: uppercase;
      font-size: clamp(1.4rem, 3vw, 3rem);
      line-height: .9; letter-spacing: -.06em;
    }
    .video-caption span {
      color: var(--red); text-transform: uppercase;
      font-size: .7rem; letter-spacing: .14em; white-space: nowrap;
    }

    /* ── PROYECTO ── */
    #proyecto {
      background: linear-gradient(90deg, rgba(236,13,13,.16), transparent 42%), rgba(0,0,0,.18);
      border-block: 1px solid rgba(236,13,13,.24);
    }
    .project-grid {
      display: grid;
      grid-template-columns: .9fr 1.1fr;
      gap: clamp(1.5rem, 5vw, 4rem);
      align-items: start;
      margin-top: 2.5rem;
    }
    .project-cover {
      min-height: 520px;
      border: 2px solid var(--paper);
      background:
        linear-gradient(rgba(236,13,13,.15), rgba(0,0,0,.25)),
        linear-gradient(135deg, #4e2b36, #151319);
      box-shadow: 14px 14px 0 #000;
      position: sticky; top: 6rem;
      overflow: hidden;
    }
    .project-cover-img {
      width: 100%; height: 100%;
      object-fit: cover; object-position: center;
      filter: contrast(1.08) saturate(0.95);
      transition: transform .35s ease, filter .35s ease;
    }
    .project-cover:hover .project-cover-img { transform: scale(1.04); filter: contrast(1.15) saturate(1.05); }

    .project-copy { display: grid; gap: 1rem; }

    .manifesto {
      padding: 1.2rem;
      border: 1px solid rgba(240,240,246,.16);
      background: rgba(240,240,246,.055);
      font-size: clamp(1rem, 1.7vw, 1.22rem);
      line-height: 1.75;
      color: rgba(240,240,246,.84);
    }
    .manifesto strong { color: var(--paper); }

    .services {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem; margin-top: .5rem;
    }
    .service {
      display: block; padding: 1rem;
      border: 2px solid rgba(240,240,246,.65);
      background: rgba(0,0,0,.20);
      box-shadow: 5px 5px 0 #000;
      color: inherit; text-decoration: none;
      transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease, background .18s ease;
    }
    .service:hover { transform: translate(3px,3px); box-shadow: 2px 2px 0 #000; border-color: var(--red); background: rgba(236,13,13,.08); }
    .service h4 {
      font-family: 'Archivo Black', sans-serif;
      color: var(--red); text-transform: uppercase;
      font-size: 1.1rem; margin-bottom: .55rem;
    }
    .service p { color: rgba(240,240,246,.76); line-height: 1.55; font-size: .92rem; }

    /* ── SOCIAL ── */
    .social-wall {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem; margin-top: 2.5rem;
    }
    .social-card {
      min-height: 190px; padding: 1rem;
      border: 2px solid var(--paper);
      background: var(--red);
      box-shadow: 8px 8px 0 #000;
      display: flex; flex-direction: column; justify-content: space-between;
      transition: transform .18s ease, box-shadow .18s ease, background .18s ease;
      text-decoration: none; color: var(--paper);
    }
    .social-card:nth-child(even) { background: var(--charcoal); }
    .social-card:hover { transform: translate(4px,4px); box-shadow: 4px 4px 0 #000; background: var(--brick); }
    .social-card span { font-size: .7rem; text-transform: uppercase; letter-spacing: .16em; color: rgba(240,240,246,.76); }
    .social-card strong {
      font-family: 'Archivo Black', sans-serif;
      font-size: clamp(1.8rem, 3vw, 3rem);
      text-transform: uppercase; line-height: .9; letter-spacing: -.06em;
    }

    footer {
      display: flex; justify-content: space-between; gap: 1rem; flex-wrap: wrap;
      padding: 2rem clamp(1rem, 4vw, 3rem);
      border-top: 1px solid var(--line);
      color: rgba(240,240,246,.64); font-size: .75rem;
      text-transform: uppercase; letter-spacing: .12em;
    }

    .reveal { opacity: 0; transform: translateY(24px); transition: .7s ease; }
    .reveal.visible { opacity: 1; transform: translateY(0); }

    @media (max-width: 980px) {
      #bio, .video-layout, .project-grid { grid-template-columns: 1fr; }
      .bio-card, .project-cover { min-height: 380px; position: relative; top: auto; }
      .image-card:nth-child(n) { grid-column: span 6; min-height: 280px; }
      .social-wall { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
      .topbar { align-items: flex-start; flex-direction: column; }
      .navlinks { justify-content: flex-start; }
      .image-grid { grid-template-columns: 1fr; }
      .image-card:nth-child(n) { grid-column: auto; }
      .services, .social-wall { grid-template-columns: 1fr; }
      .video-main { min-height: 360px; }
      .video-caption { align-items: flex-start; flex-direction: column; }
      .btn { width: 100%; }
    }
  </style>
</head>

<body>
<div class="page">

  <header class="topbar">
    <a class="brand" href="#bio"><span>David</span> Pineda</a>
    <nav class="navlinks" aria-label="Navegación principal">
      <a href="#bio">Bio</a>
      <a href="#imagenes">Imágenes</a>
      <a href="#videos">Videos</a>
      <a href="#proyecto">Proyecto</a>
      <a href="#redes">Redes</a>
    </nav>
  </header>

  <!-- 01 / BIO -->
  <section id="bio" class="section">
    <div class="bio-copy reveal">
      <div class="stamp">músico &amp; productor</div>
      <h1 class="bio-headline">Groove,<br><span class="glitch">Alma</span><br>identidad.</h1>
      <p class="bio-text">
        <strong>Convierto tu alma en música.</strong> Soy productor musical, beatmaker y músico enfocado en transformar ideas, emociones y visiones artísticas en proyectos con identidad real. Me muevo entre lo orgánico y lo urbano, mezclando influencias del jazz, el hip hop y otros lenguajes modernos para crear sonoridades vivas, profundas y diferentes. Busco que cada proyecto tenga carácter propio, que conecte emocionalmente y que haga sentir al artista realmente representado por su música.
      </p>
      <p class="bio-text">
        Además de la producción, trabajo como arreglista, bajista de sesión y músico en vivo, desarrollando desde grooves y armonías hasta estructuras y conceptos completos para cada proyecto. Mi enfoque está en entender la esencia de cada artista y convertirla en una experiencia sonora auténtica, cuidando tanto la emoción como los detalles musicales que hacen única una canción.
      </p>
      <div class="role-tags">
        <span class="tag">Bajista de sesión</span>
        <span class="tag">Productor musical</span>
        <span class="tag">Beatmaker</span>
        <span class="tag">Arreglista</span>
        <span class="tag">Hip-hop</span>
        <span class="tag">Jazz / Rock / R&amp;B</span>
      </div>
      <div class="button-row">
        <a class="btn" href="#redes">Ver redes</a>
        <a class="btn secondary" href="#proyecto">Proyecto personal</a>
      </div>
    </div>

    <aside class="bio-card reveal">
      <img src="https://i.pinimg.com/736x/86/0d/79/860d79bdaf4655315dd87553952f73f7.jpg"
           alt="Foto principal de Juan David Pineda" class="bio-main-img"/>
      <div class="parental">Original<br>Groove<br>Content</div>
    </aside>
  </section>

  <!-- 02 / IMÁGENES -->
  <section id="imagenes" class="section">
    <span class="section-kicker reveal">02 / Imagen visual</span>
    <h2 class="section-title reveal">Fotos, estética y <span class="red-word">universo</span>.</h2>
    <div class="image-grid reveal">
      <article class="image-card" data-label="Live">
        <img src="https://i.pinimg.com/736x/36/25/d9/3625d966695bb11b73a264aa40bb730e.jpg" alt="Press shot" class="portfolio-img"/>
      </article>
      <article class="image-card" data-label="Studio">
        <img src="https://i.pinimg.com/736x/c1/16/3d/c1163d9709a92765a73b77d228c256d2.jpg" alt="Estudio" class="portfolio-img"/>
      </article>
      <article class="image-card" data-label="Live">
        <img src="https://i.pinimg.com/736x/3d/4e/12/3d4e1260525308ad698817b782a7a468.jpg" alt="En vivo" class="portfolio-img"/>
      </article>
      <article class="image-card" data-label="Direccion">
        <img src="https://i.pinimg.com/736x/ff/c8/2c/ffc82c53f240cb29ccddbbe8fc03dc8b.jpg" alt="Moodboard" class="portfolio-img"/>
      </article>
      <article class="image-card" data-label="Arreglos">
        <img src="https://i.pinimg.com/736x/42/ef/8d/42ef8dbbc4625969554a3f613b886ac9.jpg" alt="Proceso creativo" class="portfolio-img"/>
      </article>
    </div>
  </section>

  <!-- 03 / VIDEOS -->
  <section id="videos" class="section">
    <span class="section-kicker reveal">03 / Videos</span>
    <h2 class="section-title reveal">Sesiones, reels y <span class="red-word">performance</span>.</h2>
    <div class="video-layout reveal">
      <a class="video-card video-main" href="__URL0__" target="_blank" rel="noopener">
        <img src="__THUMB0__" alt="Grabaciones de estudio" class="video-thumb"/>
        <div class="play">&#9654;</div>
        <div class="video-caption">
          <h3>Grabaciones de estudio</h3>
          <span>Mr / LOS FAROS</span>
        </div>
      </a>
      <div class="video-stack">
        <a class="video-card" href="__URL1__" target="_blank" rel="noopener">
          <img src="__THUMB1__" alt="Arreglos" class="video-thumb"/>
          <div class="play">&#9654;</div>
          <div class="video-caption">
            <h3>Arreglos</h3>
            <span>YouTube</span>
          </div>
        </a>
        <a class="video-card" href="__URL2__" target="_blank" rel="noopener">
          <img src="__THUMB2__" alt="Live Sevijazz 2025" class="video-thumb"/>
          <div class="play">&#9654;</div>
          <div class="video-caption">
            <h3>Live (Sevijazz 2025)</h3>
            <span>Latin jazz / Bass Impro</span>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- 04 / PROYECTO -->
  <section id="proyecto" class="section">
    <span class="section-kicker reveal">04 / Proyecto personal</span>
    <h2 class="section-title reveal">Mi lado más <span class="red-word">personal</span>.</h2>
    <div class="project-grid">
      <div class="project-cover reveal">
        <img src="https://i.pinimg.com/736x/94/8c/e7/948ce7e13a94c03b0f8783794f0be3dd.jpg"
             alt="Proyecto personal" class="project-cover-img"/>
      </div>
      <div class="project-copy reveal">
        <p class="manifesto">
          Mi proyecto personal nace de la unión entre el <strong>hip-hop old school</strong>, el sampling, el bajo eléctrico y la sensibilidad armónica del jazz. Es un espacio para contar historias desde el groove: beats con textura, melodías oscuras, baterías con peso y una estética cruda, directa y emocional.
        </p>
        <p class="manifesto">
          Más que producir por producir, busco construir una identidad completa: portada, sonido, narrativa, referencias, arreglos e intención. Cada canción tiene que sentirse como una escena, una calle, una noche o una memoria.
        </p>
        <div class="services">
          <a class="service" href="https://open.spotify.com/user/31wez2sjzsiplion6lvtg6rnyvnq?si=76fceaf982c049c5" target="_blank" rel="noopener">
            <h4>Spotify</h4>
            <p>Escucha mis lanzamientos oficiales, colaboraciones y producciones disponibles en plataformas digitales.</p>
          </a>
          <a class="service" href="https://www.youtube.com/@Pinedamusic.wav6" target="_blank" rel="noopener">
            <h4>YouTube</h4>
            <p>Mira live sessions, presentaciones, contenido visual y procesos detrás de cada proyecto.</p>
          </a>
          <a class="service" href="https://soundcloud.com/sin-oficio-688647778" target="_blank" rel="noopener">
            <h4>SoundCloud</h4>
            <p>Encuentra demos, beats, ideas en proceso y material experimental que complementa mi universo sonoro.</p>
          </a>
          <a class="service" href="https://www.instagram.com/pinedamusic.wav/?hl=es" target="_blank" rel="noopener">
            <h4>Instagram</h4>
            <p>Sigue mi proceso creativo, contenido visual, reels, sesiones y momentos del día a día como músico y productor.</p>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 05 / REDES -->
  <section id="redes" class="section">
    <span class="section-kicker reveal">05 / Links</span>
    <h2 class="section-title reveal">Conecta conmigo en <span class="red-word">redes</span>.</h2>
    <div class="social-wall reveal">
      <a class="social-card" href="https://www.instagram.com/pinedamusic.wav/?hl=es" target="_blank" rel="noopener">
        <span>Fotos / reels / proceso</span>
        <strong>Instagram</strong>
      </a>
      <a class="social-card" href="https://open.spotify.com/user/31wez2sjzsiplion6lvtg6rnyvnq" target="_blank" rel="noopener">
        <span>Lanzamientos / música</span>
        <strong>Spotify</strong>
      </a>
      <a class="social-card" href="https://www.youtube.com/@Pinedamusic.wav6" target="_blank" rel="noopener">
        <span>Videos / sesiones</span>
        <strong>YouTube</strong>
      </a>
      <a class="social-card" href="https://soundcloud.com/sin-oficio-688647778" target="_blank" rel="noopener">
        <span>Beats / demos / ideas</span>
        <strong>SoundCloud</strong>
      </a>
    </div>
  </section>

  <footer>
    <p>© 2026 — Juan David Pineda Ramirez</p>
    <p>Músico · Productor · Beatmaker · Bajista</p>
  </footer>
</div>

<script>
  // ── Resize iframe to fill parent viewport (works same-origin) ─────────────
  (function () {
    function resize() {
      try {
        var fe = window.frameElement;
        if (!fe) return;
        var top = fe.getBoundingClientRect().top;
        fe.style.height = (window.parent.innerHeight - Math.max(0, top)) + 'px';
        fe.style.width  = '100%';
      } catch (e) {}
    }
    resize();
    window.addEventListener('load', resize);
    try { window.parent.addEventListener('resize', resize); } catch (e) {}
  })();

  // ── Scroll-reveal via IntersectionObserver ────────────────────────────────
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

  // ── Anchor nav: srcdoc iframes no disparan scroll nativo con href="#id" ──
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var target = document.getElementById(this.getAttribute('href').slice(1));
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
</script>
</body>
</html>"""

# Inject pre-computed YouTube values
FULL_HTML = (FULL_HTML
    .replace("__URL0__",   VIDEOS[0]["url"])
    .replace("__THUMB0__", VIDEOS[0]["thumb"])
    .replace("__URL1__",   VIDEOS[1]["url"])
    .replace("__THUMB1__", VIDEOS[1]["thumb"])
    .replace("__URL2__",   VIDEOS[2]["url"])
    .replace("__THUMB2__", VIDEOS[2]["thumb"])
)

components.html(FULL_HTML, height=800, scrolling=True)
