from pathlib import Path
import re
root=Path('/mnt/data/v313fix')
info={
'calculadora-ipv4':('Calculadora IPv4','Analiza una IPv4 y un prefijo para obtener la red, máscara, broadcast, rango y número de hosts.','Practica direccionamiento IPv4 y comprueba tus resultados antes de llevarlos a una práctica.'),
'cidr-calculadora':('Calculadora CIDR','Convierte un prefijo CIDR en máscara, número de direcciones, hosts utilizables y tamaño de bloque.','Úsala para comprobar rápidamente cómo cambia una red al modificar el prefijo.'),
'ipv4-binario':('IPv4 a Binario','Convierte cada octeto IPv4 a 8 bits y muestra la máscara CIDR en formato decimal y binario.','Es especialmente útil para prácticas de subnetting y para justificar cálculos paso a paso.'),
'binario-ipv4':('Binario a IPv4','Convierte cuatro octetos binarios de 8 bits en una dirección IPv4 y valida el formato de entrada.','Comprueba conversiones de direccionamiento antes de continuar con una práctica de redes.'),
'puertos-protocolos':('Puertos y Protocolos','Consulta puertos habituales, su protocolo de transporte y el servicio con el que suelen relacionarse.','Sirve como referencia rápida durante prácticas de servicios de red y diagnóstico.'),
'registros-dns':('Registros DNS','Genera una referencia editable para registros A, AAAA, CNAME, MX y TXT.','Úsala para estudiar qué información contiene cada registro y documentar una configuración.'),
'mac-formateador':('Formateador MAC','Valida una dirección MAC y la muestra en formatos habituales: dos puntos, guiones, puntos o sin separadores.','Es útil para prácticas de redes locales y para documentar direcciones de dispositivos.'),
'tiempo-transferencia':('Tiempo de transferencia','Estima el tiempo necesario para transferir un archivo a partir de su tamaño y velocidad de conexión.','La estimación ayuda a comparar escenarios; no incluye latencia ni toda la sobrecarga de una red real.')}
related={
'calculadora-ipv4':[('cidr-calculadora','Calculadora CIDR'),('subnetting','Subnetting IPv4'),('ipv4-binario','IPv4 a Binario')],
'cidr-calculadora':[('calculadora-ipv4','Calculadora IPv4'),('subnetting','Subnetting IPv4'),('binario-ipv4','Binario a IPv4')],
'ipv4-binario':[('binario-ipv4','Binario a IPv4'),('calculadora-ipv4','Calculadora IPv4'),('subnetting','Subnetting IPv4')],
'binario-ipv4':[('ipv4-binario','IPv4 a Binario'),('calculadora-ipv4','Calculadora IPv4'),('subnetting','Subnetting IPv4')],
'puertos-protocolos':[('registros-dns','Registros DNS'),('http-status','Códigos HTTP'),('calculadora-ipv4','Calculadora IPv4')],
'registros-dns':[('puertos-protocolos','Puertos y Protocolos'),('parser-url','Analizador de URL'),('calculadora-ipv4','Calculadora IPv4')],
'mac-formateador':[('puertos-protocolos','Puertos y Protocolos'),('calculadora-ipv4','Calculadora IPv4'),('subnetting','Subnetting IPv4')],
'tiempo-transferencia':[('calculadora-ipv4','Calculadora IPv4'),('puertos-protocolos','Puertos y Protocolos'),('subnetting','Subnetting IPv4')]}
for slug,(title,desc,about) in info.items():
 p=root/'herramientas'/slug/'index.html';s=p.read_text()
 # Replace leftover template content
 s=s.replace('Códigos HTTP',title).replace('códigos http',title.lower())
 # Replace the generic about sentence if still present
 s=re.sub(r'<section class="mt-10 bg-slate-900.*?</section><section id="aq-specific-guide"',lambda m: f'''<section class="mt-10 bg-slate-900 border border-slate-800 rounded-2xl p-6"><h2 class="text-2xl font-bold">Sobre esta herramienta</h2><p class="text-slate-400 mt-3 leading-7">{about}</p><h2 class="text-xl font-bold mt-7">Herramientas relacionadas</h2><div class="flex flex-wrap gap-4 mt-3">'''+''.join(f'<a href="../{sl}/" class="text-emerald-400 hover:underline">{nm}</a>' for sl,nm in related[slug])+'''</div></section><section id="aq-specific-guide"''',s,count=1,flags=re.S)
 # Tailor guide title/content leftovers
 s=s.replace('Cómo aprovechar '+title, 'Cómo aprovechar '+title)
 s=re.sub(r'<span class="aq-badge">Guía de uso · Redes y sistemas</span><h2>Cómo aprovechar .*?</h2><div class="aq-grid">.*?</div></section>', f'''<span class="aq-badge">Guía de uso · Redes y sistemas</span><h2>Cómo aprovechar {title}</h2><div class="aq-grid"><div><h3>1. Antes de empezar</h3><p>Define qué dato necesitas obtener y revisa el formato de entrada. En una práctica de FP, anota los valores iniciales para poder justificar después el resultado.</p></div><div><h3>2. Realiza la comprobación</h3><p>Introduce un caso sencillo, ejecuta la herramienta y compara el resultado con el procedimiento que hayas seguido manualmente.</p></div><div><h3>3. Interpreta el resultado</h3><p>No te quedes solo con el número final: revisa qué representa, qué rango cubre y qué datos han cambiado respecto al caso inicial.</p></div><div><h3>4. Reutiliza el resultado</h3><p>Si es una práctica, guarda los datos y la conclusión. Así puedes explicar el proceso y detectar más fácilmente un error de configuración.</p></div></div></section>''',s,count=1,flags=re.S)
 p.write_text(s)

# fix incorrect stylesheet path inherited by all tool pages
for p in (root/'herramientas').glob('*/index.html'):
 s=p.read_text()
 s=s.replace('href="../assets/site-polish-v33.css"','href="../../assets/site-polish-v33.css"')
 p.write_text(s)
