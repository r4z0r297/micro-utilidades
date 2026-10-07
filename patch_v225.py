from pathlib import Path
import re
ROOT=Path('/mnt/data/appquick_v22_5')
net_pages={
 'calculadora-ipv4','cidr-calculadora','ipv4-binario','binario-ipv4','puertos-protocolos','registros-dns','mac-formateador','tiempo-transferencia','subnetting','http-status','parser-url'
}
# Make every network tool use the same category kicker/header pattern as the good subnetting page.
for slug in net_pages:
    p=ROOT/'herramientas'/slug/'index.html'
    s=p.read_text(encoding='utf-8')
    # Replace the old compact title wrapper if present.
    m=re.search(r'<div class="aq-tool-title"><h1>(.*?)</h1><p>(.*?)</p></div>',s,re.S)
    if m:
        title,desc=m.group(1),m.group(2)
        repl=f'<div class="mb-8"><p class="text-emerald-400 text-sm font-bold">Redes / Networking</p><h1 class="text-4xl md:text-5xl font-black mt-2">{title}</h1><p class="text-slate-400 mt-3 max-w-5xl text-lg md:text-xl">{desc}</p></div>'
        s=s[:m.start()]+repl+s[m.end():]
    # Correct obvious stale metadata accidentally inherited from other pages.
    # Canonical is already correct; only fix OG description/url and JSON-LD URL if stale.
    s=s.replace('content="Consulta el significado de códigos HTTP." name="description"', 'content="Calcula red, máscara, broadcast, rango y hosts a partir de una IPv4 y un prefijo." name="description"') if slug=='calculadora-ipv4' else s
    s=s.replace('property="og:description"', 'property="og:description"', 1)
    # For calc IPv4 specifically, replace the stale HTTP status OG values.
    if slug=='calculadora-ipv4':
        s=s.replace('content="Consulta el significado de códigos HTTP." property="og:description"','content="Calcula red, máscara, broadcast, rango y hosts a partir de una IPv4 y un prefijo." property="og:description"')
        s=s.replace('content="https://appquickutils.com/herramientas/http-status/" property="og:url"','content="https://appquickutils.com/herramientas/calculadora-ipv4/" property="og:url"')
        s=s.replace('"url":"https://appquickutils.com/herramientas/http-status/"','"url":"https://appquickutils.com/herramientas/calculadora-ipv4/"')
    p.write_text(s,encoding='utf-8')

# Homepage: Redes · FP card is informational only, not a link and no hover interaction.
p=ROOT/'index.html'
s=p.read_text(encoding='utf-8')
old='<a class="cat" href="herramientas/?cat=redes"><span class="cat-icon"><i class="fa-solid fa-network-wired"></i></span><span><h3>Redes · FP</h3><p>IPv4, CIDR, DNS y puertos</p></span><span class="cat-count">11</span></a>'
new='<div class="cat cat-static" aria-label="Categoría informativa: Redes · FP"><span class="cat-icon"><i class="fa-solid fa-network-wired"></i></span><span><h3>Redes · FP</h3><p>IPv4, CIDR, DNS y puertos</p></span><span class="cat-count">11</span></div>'
if old not in s:
    raise SystemExit('Homepage Redes card pattern not found')
s=s.replace(old,new)
# Add a hard override so the card stays visually static on hover.
needle='.cat:hover{border-color:#2b4a5b}'
s=s.replace(needle, needle+' .cat-static{cursor:default}.cat-static:hover{border-color:#1d3145} .cat-static .cat-icon{transition:none}',1)
p.write_text(s,encoding='utf-8')
