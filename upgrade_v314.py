from pathlib import Path
import re, shutil, html, json
from bs4 import BeautifulSoup
root=Path('/mnt/data/v313fix')
assets=root/'assets'

# 1) New common refinement CSS
css='''\n/* AppQuickUtils V31.4 — functional + layout refinement */
.aq-v31-cta-final{width:100%!important;max-width:1720px!important;margin:54px auto 0!important;padding:30px 38px!important;display:flex!important;align-items:center!important;justify-content:space-between!important;gap:32px!important;box-sizing:border-box!important;border:1px solid #24415e!important;border-radius:22px!important;background:linear-gradient(105deg,#0b1b2e,#081423 65%,#092333)!important;min-height:150px!important}
.aq-v31-cta-final .cta-copy{min-width:0!important}.aq-v31-cta-final .cta-kicker{display:block!important;color:#5eead4!important;font-size:.72rem!important;text-transform:uppercase!important;letter-spacing:.14em!important;font-weight:900!important;margin-bottom:8px!important}.aq-v31-cta-final h2{margin:0 0 7px!important;font-size:clamp(1.45rem,2.4vw,2.1rem)!important;line-height:1.15!important;color:#f8fafc!important}.aq-v31-cta-final p{margin:0!important;color:#9fb1c4!important;line-height:1.65!important;max-width:820px!important}.aq-v31-cta-final a{flex:0 0 auto!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:8px!important;padding:14px 20px!important;border-radius:12px!important;background:linear-gradient(135deg,#34d399,#22d3ee)!important;color:#04131a!important;font-weight:900!important;text-decoration:none!important;white-space:nowrap!important;box-shadow:0 10px 28px rgba(34,211,238,.12)!important}
/* Guide cards: fixed reading order */
.aq-guide-list{max-width:1720px!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:22px!important}
.aq-guide-list a{position:relative!important;min-height:310px!important;padding:28px 30px 26px!important;display:flex!important;flex-direction:column!important;box-sizing:border-box!important}
.aq-guide-list a:before{position:absolute!important;left:auto!important;right:22px!important;top:20px!important;width:38px!important;height:38px!important;display:flex!important;align-items:center!important;justify-content:center!important}
.aq-guide-number{display:inline-flex!important;align-items:center!important;justify-content:center!important;width:36px!important;height:36px!important;border-radius:11px!important;background:rgba(52,211,153,.09)!important;border:1px solid rgba(52,211,153,.25)!important;color:#6ee7b7!important;font-size:.75rem!important;font-weight:900!important;margin-bottom:18px!important}
.aq-guide-list h2{padding-right:48px!important;font-size:1.25rem!important;line-height:1.28!important;margin:0 0 10px!important}
.aq-guide-summary{margin:0 0 18px!important;color:#a9bacb!important;line-height:1.7!important}
.aq-guide-flow{display:grid!important;gap:8px!important;margin-top:auto!important;padding-top:4px!important}
.aq-guide-flow span{display:block!important;color:#d7e1ea!important;font-size:.84rem!important;line-height:1.5!important;padding-left:0!important}
.aq-guide-flow b{color:#5eead4!important}
.aq-guide-open{display:inline-flex!important;align-items:center!important;margin-top:18px!important;padding-top:14px!important;border-top:1px solid #1c334a!important;color:#5eead4!important;font-size:.8rem!important;font-weight:900!important}
/* Resources: cards read as routes, not empty boxes */
.aq-grid{max-width:1720px!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:22px!important}
.aq-card{min-height:300px!important;padding:28px!important;display:flex!important;flex-direction:column!important;box-sizing:border-box!important}
.aq-card .aq-card-detail{margin-top:9px!important;color:#9fb1c4!important;line-height:1.72!important}
.aq-card:after{margin-top:auto!important;padding-top:18px!important}
.aq-check{max-width:1720px!important}
/* Project page: clear hierarchy and no inline collisions */
.aq-project-grid{max-width:1720px!important;grid-template-columns:repeat(4,minmax(0,1fr))!important}
.aq-project-card{min-height:205px!important;justify-content:flex-start!important}
.aq-project-card strong{font-size:1.15rem!important}.aq-project-card span:last-child{font-size:.92rem!important;line-height:1.72!important}
.aq-project-section{max-width:1720px!important}.aq-project-section>p{max-width:1250px!important}
/* Long tool educational sections use the screen instead of leaving a giant right gap. */
.aq-tool-guide,.aq-tool-guide .aq-grid,.aq-tool-guide .aq-check{max-width:1720px!important;width:100%!important;box-sizing:border-box!important}
.aq-article .aq-tool-guide>p,.aq-article .aq-tool-guide>h2,.aq-article .aq-tool-guide>h3{max-width:1450px!important}
/* Network category */
.aq-network-category{margin-top:0!important;border-color:rgba(34,211,238,.28)!important;background:linear-gradient(135deg,rgba(8,31,48,.96),rgba(8,20,35,.96))!important}
.aq-network-category .network-badge{color:#67e8f9!important;background:rgba(34,211,238,.08)!important;border:1px solid rgba(34,211,238,.22)!important}
@media(max-width:1150px){.aq-guide-list,.aq-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}.aq-project-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:700px){.aq-v31-cta-final{display:grid!important;grid-template-columns:1fr!important;padding:24px!important;margin-top:38px!important}.aq-v31-cta-final a{width:max-content!important}.aq-guide-list,.aq-grid,.aq-project-grid{grid-template-columns:1fr!important}.aq-guide-list a{min-height:0!important;padding:24px!important}.aq-guide-list h2{padding-right:0!important}.aq-card{min-height:0!important}.aq-project-card{min-height:0!important}}
'''
(assets/'site-polish-v34.css').write_text(css,encoding='utf-8')

# Add stylesheet to all HTML with correct relative path
for p in root.rglob('*.html'):
    s=p.read_text(errors='ignore')
    if 'site-polish-v34.css' in s: continue
    rel=os_rel = Path(__import__('os').path.relpath(assets/'site-polish-v34.css',p.parent)).as_posix()
    s=s.replace('</head>',f'<link rel="stylesheet" href="{rel}"></head>',1)
    p.write_text(s,encoding='utf-8')

# 2) Home CTA cleanup
home=root/'index.html'
s=home.read_text()
old=re.search(r'<section class="aq-v29-container aq-v29-cta">.*?</section>',s,re.S)
if old:
    new='''<section class="aq-v31-cta-final" aria-labelledby="catalog-cta-title"><div class="cta-copy"><span class="cta-kicker">Catálogo completo</span><h2 id="catalog-cta-title">¿No sabes qué herramienta necesitas?</h2><p>Busca por tarea, formato o palabra clave y filtra el catálogo hasta encontrar la utilidad que encaja con lo que quieres resolver.</p></div><a href="herramientas/">Ver todas las herramientas <i class="fa-solid fa-arrow-right"></i></a></section>'''
    s=s[:old.start()]+new+s[old.end():]
# ensure no accidental old pseudo CTA text
s=s.replace('.aq-v29-hero-main:after{content:"Explora todo el catálogo desde Herramientas";display:block;margin-top:16px;color:#64748b;font-size:.86rem}', '.aq-v29-hero-main:after{content:"El catálogo completo está en Herramientas";display:block;margin-top:16px;color:#64748b;font-size:.86rem}')
home.write_text(s,encoding='utf-8')

# 3) Guides cards: replace with structured, ordered cards
p=root/'guias/index.html'; s=p.read_text()
container=re.search(r'<div class="aq-guide-list">.*?</div></main>',s,re.S)
if container:
    # Extract existing anchors from old block
    block=container.group(0)
    cards=re.findall(r'<a href="([^"]+)"><h2>(.*?)</h2><p>(.*?)</p></a>',block,re.S)
    parts=[]
    for i,(href,title,desc) in enumerate(cards,1):
        # Contextual step text based on title
        t=BeautifulSoup(title,'html.parser').get_text(' ',strip=True)
        if any(x in t.lower() for x in ['subnetting','cidr','vlsm','ipv4','ipv6','dns','dhcp','osi']):
            flow=('1. Entiende el concepto y los datos de entrada.','2. Resuelve un ejemplo con valores reales.','3. Comprueba el resultado con la herramienta relacionada.')
        elif any(x in t.lower() for x in ['json','html','css','sql','regex','base64']):
            flow=('1. Identifica la estructura o sintaxis correcta.','2. Practica con un ejemplo y localiza los errores.','3. Valida el resultado antes de reutilizarlo.')
        elif any(x in t.lower() for x in ['pdf','imagenes']):
            flow=('1. Elige el formato y objetivo del archivo.','2. Aplica el procedimiento y revisa la salida.','3. Comprueba tamaño, calidad y contenido.')
        elif any(x in t.lower() for x in ['contrase','datos']):
            flow=('1. Identifica qué información estás manejando.','2. Sigue una práctica segura y evita datos sensibles.','3. Comprueba el resultado antes de compartirlo.')
        elif any(x in t.lower() for x in ['nota','estudio','herramienta']):
            flow=('1. Define el objetivo y el tiempo disponible.','2. Divide la tarea en pasos medibles.','3. Comprueba qué has conseguido y ajusta el siguiente paso.')
        else:
            flow=('1. Comprende qué problema resuelve la guía.','2. Sigue el procedimiento con un ejemplo.','3. Comprueba el resultado antes de continuar.')
        parts.append(f'''<a href="{href}"><span class="aq-guide-number">{i:02d}</span><h2>{title}</h2><p class="aq-guide-summary">{desc}</p><div class="aq-guide-flow"><span><b>1</b> · {flow[0][3:]}</span><span><b>2</b> · {flow[1][3:]}</span><span><b>3</b> · {flow[2][3:]}</span></div><span class="aq-guide-open">Abrir guía <i class="fa-solid fa-arrow-right"></i></span></a>''')
    newblock='<div class="aq-guide-list">'+''.join(parts)+'</div></main>'
    s=s[:container.start()]+newblock+s[container.end():]
p.write_text(s,encoding='utf-8')

# 4) Add network tools to catalog + new category
cat=root/'herramientas/index.html'; s=cat.read_text()
# Insert network category before developers
network='''<section class="category aq-network-category" data-cat-section="redes"><div class="p-5 sm:p-7 mb-5 rounded-2xl border border-cyan-400/20 bg-cyan-400/5"><span class="network-badge inline-flex rounded-full px-3 py-1 text-xs font-black">REDES · FP</span><h2 class="text-2xl md:text-3xl font-black mt-3">Redes / Networking</h2><p class="text-slate-400 mt-2 max-w-3xl">Herramientas para ASIR, SMR, DAM y DAW: direccionamiento IPv4, CIDR, puertos, DNS, MAC, transferencia y comprobaciones básicas de red.</p></div><div class="aq-tool-grid grid gap-4">'''
nettools=[
('calculadora-ipv4','Calculadora IPv4','Red, máscara, broadcast, rango y hosts.'),
('cidr-calculadora','Calculadora CIDR','Prefijo, máscara, hosts y tamaño de subred.'),
('ipv4-binario','IPv4 a Binario','Convierte una IPv4 y su máscara a binario.'),
('binario-ipv4','Binario a IPv4','Convierte cuatro octetos binarios a IPv4.'),
('puertos-protocolos','Puertos y Protocolos','Consulta puertos habituales y su protocolo.'),
('registros-dns','Registros DNS','Genera una referencia clara para A, AAAA, CNAME, MX y TXT.'),
('mac-formateador','Formateador MAC','Normaliza una dirección MAC en formatos habituales.'),
('tiempo-transferencia','Tiempo de transferencia','Estima cuánto tarda una transferencia según tamaño y velocidad.'),
('subnetting','Subnetting IPv4','Divide redes, analiza CIDR y calcula supernetting.'),
('http-status','Códigos HTTP','Consulta códigos de respuesta HTTP frecuentes.'),
('parser-url','Analizador de URL','Separa protocolo, host, ruta, query y fragmento.'),
]
for slug,name,desc in nettools:
    network+=f'<a data-name="{html.escape((name+" "+desc).lower())}" data-cat="redes" href="{slug}/" class="toolcard bg-slate-900 border border-slate-800 hover:border-cyan-400/50 rounded-xl p-4 transition"><div class="font-bold">{name}</div><div class="text-xs text-slate-500 mt-1">{desc}</div></a>'
network+='</div></section>'
s=s.replace('<div class="space-y-12 mt-5"><section class="category" data-cat-section="desarrolladores">', '<div class="space-y-12 mt-5">'+network+'<section class="category" data-cat-section="desarrolladores">',1)
s=s.replace("const icons={desarrolladores:'👨‍💻',texto", "const icons={redes:'🌐',desarrolladores:'👨‍💻',texto",1)
s=s.replace("const labels={desarrolladores:'Desarrollo',texto", "const labels={redes:'Redes · FP',desarrolladores:'Desarrollo',texto",1)
cat.write_text(s,encoding='utf-8')

# 5) Create new network tool pages from http-status template, with network config and tailored metadata.
template=(root/'herramientas/http-status/index.html').read_text()
network_pages={
'calculadora-ipv4':('Calculadora IPv4','Calcula red, máscara, broadcast, rango y hosts a partir de una IPv4 y un prefijo.'),
'cidr-calculadora':('Calculadora CIDR','Convierte un prefijo CIDR en máscara, número de hosts y tamaño de bloque.'),
'ipv4-binario':('IPv4 a Binario','Convierte una IPv4 en cuatro octetos binarios y muestra la máscara si la indicas.'),
'binario-ipv4':('Binario a IPv4','Convierte cuatro octetos binarios en una dirección IPv4 válida.'),
'puertos-protocolos':('Puertos y Protocolos','Consulta puertos de red frecuentes, su protocolo y su uso habitual.'),
'registros-dns':('Registros DNS','Genera ejemplos de registros A, AAAA, CNAME, MX y TXT para estudiar y documentar configuraciones.'),
'mac-formateador':('Formateador MAC','Valida y normaliza una dirección MAC en formatos con dos puntos, guiones o sin separadores.'),
'tiempo-transferencia':('Tiempo de transferencia','Calcula una estimación del tiempo necesario para transferir un archivo según su tamaño y velocidad.'),
}
for slug,(title,desc) in network_pages.items():
    d=root/'herramientas'/slug; d.mkdir(exist_ok=True)
    s=template
    s=re.sub(r'<title>.*?</title>',f'<title>{html.escape(title)} | AppQuickUtils</title>',s,count=1,flags=re.S)
    s=re.sub(r'<meta name="description" content=".*?">',f'<meta name="description" content="{html.escape(desc)}">',s,count=1)
    s=re.sub(r'<link rel="canonical" href="[^"]+">',f'<link rel="canonical" href="https://appquickutils.com/herramientas/{slug}/">',s,count=1)
    # Config before tool.js
    s=s.replace('</head>',f'<script>window.TOOL_CONFIG={{type:"{slug}"}};</script></head>',1)
    # Replace visible header title and lead where present
    s=re.sub(r'<h1[^>]*>.*?</h1>',f'<h1>{html.escape(title)}</h1>',s,count=1,flags=re.S)
    s=re.sub(r'<p[^>]*>.*?</p>',f'<p>{html.escape(desc)}</p>',s,count=1,flags=re.S)
    # add CSS v34 relative path (template may not have it)
    if 'site-polish-v34.css' not in s: s=s.replace('</head>','<link rel="stylesheet" href="../../assets/site-polish-v34.css"></head>',1)
    d.joinpath('index.html').write_text(s,encoding='utf-8')

# 6) Add network types to tool.js via a compact custom branch before subnetting
js=assets/'tool.js'; s=js.read_text()
marker="function customTool(type){\n const root=$('tool-app'); if(!root) return false;\n if(type==='subnetting'){"
insert=r'''function customTool(type){
 const root=$('tool-app'); if(!root) return false;
 if(['calculadora-ipv4','cidr-calculadora','ipv4-binario','binario-ipv4','puertos-protocolos','registros-dns','mac-formateador','tiempo-transferencia'].includes(type)){
  const defs={
   'calculadora-ipv4':{title:'Calculadora IPv4',desc:'Introduce una IPv4 y un prefijo para obtener red, máscara, broadcast, rango y hosts.',fields:'<input id="nIp" class="aq-input" value="192.168.1.25" placeholder="192.168.1.25"><input id="nPre" class="aq-input" type="number" min="0" max="32" value="24" placeholder="24">',run(){const v=$('nIp').value.trim(),p=Number($('nPre').value);return netAnalyze(v,p)}},
   'cidr-calculadora':{title:'Calculadora CIDR',desc:'Obtén máscara, tamaño de bloque y hosts disponibles a partir de un prefijo.',fields:'<input id="nPre" class="aq-input" type="number" min="0" max="32" value="24" placeholder="24">',run(){const p=Number($('nPre').value);if(!Number.isInteger(p)||p<0||p>32)throw Error('El prefijo debe estar entre /0 y /32.');const total=2**(32-p),usable=p>=31?total:Math.max(0,total-2);return `CIDR: /${p}\nMáscara: ${netMask(p)}\nDirecciones: ${total.toLocaleString('es-ES')}\nHosts utilizables: ${usable.toLocaleString('es-ES')}\nTamaño de bloque: ${total.toLocaleString('es-ES')}`}},
   'ipv4-binario':{title:'IPv4 a Binario',desc:'Convierte una IPv4 a sus cuatro octetos binarios y permite comprobar una máscara CIDR.',fields:'<input id="nIp" class="aq-input" value="192.168.1.25" placeholder="192.168.1.25"><input id="nPre" class="aq-input" type="number" min="0" max="32" value="24" placeholder="24">',run(){const ip=$('nIp').value.trim(),p=Number($('nPre').value);validateIp(ip);if(!Number.isInteger(p)||p<0||p>32)throw Error('Prefijo no válido.');return `IPv4: ${ip}\nBinario: ${ip.split('.').map(x=>Number(x).toString(2).padStart(8,'0')).join('.')}\nMáscara: ${netMask(p)}\nMáscara binaria: ${netMask(p).split('.').map(x=>Number(x).toString(2).padStart(8,'0')).join('.')}`}},
   'binario-ipv4':{title:'Binario a IPv4',desc:'Convierte cuatro octetos binarios de 8 bits en una IPv4.',fields:'<input id="nBin" class="aq-input" value="11000000.10101000.00000001.00011001" placeholder="11000000.10101000.00000001.00011001">',run(){const v=$('nBin').value.trim(),parts=v.split(/[. ]+/);if(parts.length!==4||parts.some(x=>!/^[01]{8}$/.test(x)))throw Error('Usa cuatro octetos de 8 bits separados por puntos.');return `IPv4: ${parts.map(x=>parseInt(x,2)).join('.')}`}},
   'puertos-protocolos':{title:'Puertos y Protocolos',desc:'Consulta puertos habituales para estudiar servicios de red y diagnóstico.',fields:'<input id="nPort" class="aq-input" type="number" min="0" max="65535" value="443" placeholder="443">',run(){const p=Number($('nPort').value);const db={20:['TCP','FTP datos'],21:['TCP','FTP control'],22:['TCP','SSH'],23:['TCP','Telnet'],25:['TCP','SMTP'],53:['TCP/UDP','DNS'],67:['UDP','DHCP servidor'],68:['UDP','DHCP cliente'],80:['TCP','HTTP'],110:['TCP','POP3'],123:['UDP','NTP'],143:['TCP','IMAP'],161:['UDP','SNMP'],443:['TCP','HTTPS'],445:['TCP','SMB'],587:['TCP','SMTP envío'],993:['TCP','IMAPS'],995:['TCP','POP3S']};if(!Number.isInteger(p)||p<0||p>65535)throw Error('El puerto debe estar entre 0 y 65535.');const x=db[p];return x?`Puerto: ${p}\nProtocolo: ${x[0]}\nUso habitual: ${x[1]}`:`Puerto: ${p}\nNo hay una referencia integrada para este puerto. Comprueba la documentación del servicio.`}},
   'registros-dns':{title:'Registros DNS',desc:'Genera una referencia editable para los registros DNS más habituales.',fields:'<select id="nDns" class="aq-input"><option>A</option><option>AAAA</option><option>CNAME</option><option>MX</option><option>TXT</option></select><input id="nHost" class="aq-input" value="www" placeholder="Host"><input id="nValue" class="aq-input" value="203.0.113.10" placeholder="Valor">',run(){const t=$('nDns').value,h=$('nHost').value.trim()||'@',v=$('nValue').value.trim();if(!v)throw Error('Introduce un valor.');const examples={A:'IPv4 del servidor',AAAA:'IPv6 del servidor',CNAME:'Nombre canónico de destino',MX:'Servidor de correo + prioridad',TXT:'Texto de verificación o política'};return `Tipo: ${t}\nHost: ${h}\nValor: ${v}\nUso: ${examples[t]}\n\nNota: sustituye los datos de ejemplo por los valores de tu proveedor DNS.`}},
   'mac-formateador':{title:'Formateador MAC',desc:'Normaliza una dirección MAC y comprueba que tenga 48 bits.',fields:'<input id="nMac" class="aq-input" value="00:1A:2B:3C:4D:5E" placeholder="00:1A:2B:3C:4D:5E">',run(){const raw=$('nMac').value.trim().replace(/[^0-9a-f]/gi,'').toUpperCase();if(!/^[0-9A-F]{12}$/.test(raw))throw Error('Introduce 12 dígitos hexadecimales.');return `Colon: ${raw.match(/../g).join(':')}\nGuiones: ${raw.match(/../g).join('-')}\nPuntos: ${raw.match(/.{4}/g).join('.')}\nPlano: ${raw}`}},
   'tiempo-transferencia':{title:'Tiempo de transferencia',desc:'Calcula una estimación del tiempo necesario para mover un archivo.',fields:'<input id="nSize" class="aq-input" type="number" value="700" min="0" placeholder="Tamaño"><select id="nUnit" class="aq-input"><option value="MB">MB</option><option value="GB">GB</option><option value="KB">KB</option></select><input id="nSpeed" class="aq-input" type="number" value="100" min="0.001" placeholder="Velocidad Mbps">',run(){const size=Number($('nSize').value),unit=$('nUnit').value,speed=Number($('nSpeed').value);if(!(size>=0&&speed>0))throw Error('Revisa tamaño y velocidad.');const bits=size*(unit==='GB'?1e9:unit==='MB'?1e6:1e3)*8,sec=bits/(speed*1e6);const h=Math.floor(sec/3600),m=Math.floor(sec%3600/60),ss=Math.round(sec%60);return `Tamaño: ${size} ${unit}\nVelocidad: ${speed} Mbps\nTiempo estimado: ${h} h ${m} min ${ss} s\n\nLa estimación no incluye latencia, sobrecarga ni variaciones de la conexión.`}}
  };
  function validateIp(ip){const p=ip.split('.').map(Number);if(p.length!==4||p.some(n=>!Number.isInteger(n)||n<0||n>255))throw Error('Introduce una IPv4 válida.');}
  function netMask(pre){if(!Number.isInteger(pre)||pre<0||pre>32)throw Error('El prefijo debe estar entre /0 y /32.');const m=pre===0?0:(0xffffffff<<(32-pre))>>>0;return [(m>>>24)&255,(m>>>16)&255,(m>>>8)&255,m&255].join('.')}
  function ipInt(ip){validateIp(ip);const p=ip.split('.').map(Number);return (((p[0]*256+p[1])*256+p[2])*256+p[3])>>>0}
  function ipStr(n){return [(n>>>24)&255,(n>>>16)&255,(n>>>8)&255,n&255].join('.')}
  function netAnalyze(ip,pre){const v=ipInt(ip),m=pre===0?0:(0xffffffff<<(32-pre))>>>0,n=(v&m)>>>0,b=(n|(~m))>>>0,total=2**(32-pre),usable=pre>=31?total:Math.max(0,total-2);return `IPv4: ${ip}\nCIDR: ${ip}/${pre}\nRed: ${ipStr(n)}\nMáscara: ${netMask(pre)}\nBroadcast: ${ipStr(b)}\nPrimer host: ${pre>=31?ipStr(n):ipStr(n+1)}\nÚltimo host: ${pre>=31?ipStr(b):ipStr(b-1)}\nHosts utilizables: ${usable.toLocaleString('es-ES')}`}
  const d=defs[type];root.innerHTML=`<section class="aq-surface p-5 sm:p-7"><div class="grid xl:grid-cols-3 gap-5"><div class="xl:col-span-2"><span class="block text-xs uppercase tracking-widest text-cyan-300 font-black mb-2">Redes · FP</span><h2 class="text-2xl font-black text-white">${d.title}</h2><p class="text-sm text-slate-400 mt-2 mb-5">${d.desc}</p><div class="grid sm:grid-cols-2 gap-3">${d.fields}</div><div class="aq-calc-actions"><button id="networkRun" class="aq-primary">Calcular resultado</button><button id="networkClear" class="aq-secondary">Limpiar</button><button id="networkCopy" class="aq-secondary">Copiar</button></div></div><div class="aq-calc-result"><div class="aq-result-top"><span>Resultado</span><span class="text-xs text-slate-500">Comprobación local</span></div><pre id="networkOut" class="aq-result-value">Introduce los datos y calcula.</pre></div></div></section>`;
  const out=$('networkOut');$('networkRun').onclick=()=>{try{out.textContent=d.run()}catch(e){out.textContent='Error: '+e.message}};$('networkClear').onclick=()=>location.reload();$('networkCopy').onclick=async()=>{try{await navigator.clipboard.writeText(out.textContent);$('networkCopy').textContent='Copiado';setTimeout(()=>$('networkCopy').textContent='Copiar',1000)}catch{}};return true;
 }
 if(type==='subnetting'){'''
if marker not in s: raise SystemExit('marker not found')
s=s.replace(marker,insert,1)
js.write_text(s,encoding='utf-8')

# 7) Add tool configs/meta for new pages? customTool handles before generic, but config needed.
# Existing template may still have old TOOL_CONFIG type http-status; replacement above only added new script before head, but duplicate TOOL_CONFIG isn't a problem if later script overwrites.

# 8) Fix all new pages config duplicate and headings more precisely: remove old inline TOOL_CONFIG if present and set one.
for slug in network_pages:
 p=root/'herramientas'/slug/'index.html'; s=p.read_text()
 s=re.sub(r'<script>window\.TOOL_CONFIG=.*?</script>','',s,flags=re.S)
 s=s.replace('</head>',f'<script>window.TOOL_CONFIG={{type:"{slug}"}};</script></head>',1)
 # replace first main h1 and paragraph after main more reliably
 s=re.sub(r'(<main[^>]*>).*?(<div[^>]*id="tool-app")',lambda m:m.group(1)+f'<div class="aq-tool-title"><h1>{html.escape(network_pages[slug][0])}</h1><p>{html.escape(network_pages[slug][1])}</p></div>'+m.group(2),s,count=1,flags=re.S)
 p.write_text(s,encoding='utf-8')

# 9) Add network category to homepage? No, user requested category inside all tools; keep home clean.

# 10) Rebuild sitemap from actual HTML routes
urls=['']
for p in root.rglob('index.html'):
    rel=p.relative_to(root).parent.as_posix()
    if rel=='.': continue
    urls.append(rel+'/')
urls=sorted(set(urls))
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>https://appquickutils.com/{u}</loc></url>\n' for u in urls)+'</urlset>\n'
(root/'sitemap.xml').write_text(sm,encoding='utf-8')

# 11) Update README
(root/'README_ADSENSE_QUALITY.md').write_text('''# AppQuickUtils V31.4\n\nCambios principales:\n- Auditoría y endurecimiento de las páginas de herramientas.\n- Nuevo bloque Redes · FP dentro del catálogo principal.\n- Nuevas herramientas de redes con cálculos locales.\n- CTA final de inicio corregido y único.\n- Guías con orden de lectura: concepto → práctica → comprobación.\n- Mejoras de ancho y jerarquía en Guías, Recursos y Proyecto.\n- Sitemap regenerado desde las páginas reales.\n\nAntes de publicar: probar manualmente varias herramientas, especialmente las de archivos que cargan librerías externas.\n''',encoding='utf-8')
print('done')
