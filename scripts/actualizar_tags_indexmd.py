import os
import yaml
from pathlib import Path

# Ruta a la carpeta de posts (actualiza esto con tu ruta real)
base_path = Path('/Users/ealeman/Desktop/blog/content/es/posts')

entry_map = {'endurecimiento-servidor-ubuntu/ubuntu-hardening/': {'tags': ['ssh', 'ufw', 'fail2ban', 'linux', 'seguridad', 'autenticación', 'proxyjump'], 'categories': ['servidores', 'seguridad', 'ubuntu']}, 'nano-node/nano-node-rpc/': {'tags': ['nano', 'blockchain', 'rpc', 'criptomonedas', 'nodo', 'docker'], 'categories': ['nano', 'blockchain']}, 'plut.69.2/': {'tags': ['Plutarco', 'biografía', 'historia', 'Tito Flaminino', 'Grecia'], 'categories': ['historia', 'Grecia', 'antigüedad']}, 'la-naturaleza-de-la-computación/': {'tags': ['filosofía', 'computación', 'lógica', 'máquinas de Turing', 'conciencia'], 'categories': ['filosofía', 'computación']}, 'violencia-civilizacion/de-alejandro-a-ucrania/': {'tags': ['guerra', 'Alejandro Magno', 'Ucrania', 'historia', 'imperios', 'globalización'], 'categories': ['geopolítica', 'historia', 'ensayos']}, 'identidad-de-euler/': {'tags': ['Euler', 'matemáticas', 'identidades', 'números complejos', 'historia de la ciencia'], 'categories': ['matemáticas', 'historia de la ciencia']}, 'el-pensar-del-ser-en-heidegger/': {'tags': ['Heidegger', 'ontología', 'ser', 'filosofía continental', 'existencia'], 'categories': ['filosofía', 'ontología']}, 'de-platon-a-penrose/': {'tags': ['filosofía', 'Penrose', 'Platonismo', 'conciencia', 'computación'], 'categories': ['filosofía', 'computación', 'consciencia']}, 'da-vinci/': {'tags': ['Leonardo da Vinci', 'botánica', 'biomecánica', 'cuadernos', 'regla de los árboles'], 'categories': ['arte renacentista', 'historia de la ciencia']}, 'amanecer-de-todo/': {'tags': ['David Graeber', 'David Wengrow', 'prehistoria', 'anarquismo', 'historia'], 'categories': ['antropología', 'historia', 'ensayos']}, 'la-polis-hansen/': {'tags': ['Herman Hansen', 'polis', 'Grecia', 'ciudad-estado', 'democracia antigua'], 'categories': ['historia', 'Grecia', 'polis']}, 'el-número-cristiano-y-sus-implicaciones/': {'tags': ['cristianismo', 'matemáticas', 'historia', 'simbología', 'fe'], 'categories': ['cristianismo', 'historia de las ideas']}, 'interpretando-a-platón/': {'tags': ['Platón', 'filosofía antigua', 'interpretación', 'idealismo', 'Academia'], 'categories': ['filosofía', 'Platón']}, 'fraile-tomás-de-aquino/': {'tags': ['Tomás de Aquino', 'Escolástica', 'filosofía medieval', 'teología', 'Aristóteles'], 'categories': ['filosofía', 'medioevo', 'teología']}, 'investigacion-ciudadana/digital-humanities/': {'tags': ['Humanidades Digitales', 'digitalización', 'ciudadanía', 'acceso abierto', 'TEI'], 'categories': ['digital humanities', 'citizen science']}, 'xxi-la-estructura-de-los-anales/': {'tags': ['Tácito', 'Anales', 'estructura', 'historiografía romana', 'Roma'], 'categories': ['historia', 'Tácito', 'anales']}, 'el-último-emperador-pagano/': {'tags': ['Juliano', 'paganismo', 'Roma', 'imperio tardío', 'cristianismo'], 'categories': ['historia', 'Roma', 'emperadores']}, 'procopio-y-el-siglo-sexto/': {'tags': ['Procopio', 'historia bizantina', 'siglo VI', 'Justinianeo', 'Imperio romano de Oriente'], 'categories': ['historia', 'Procopio', 'Bizancio']}}

def update_front_matter(md_path, tags, categories):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if lines[0].strip() != '---':
        print(f'Se omite {md_path.name}: no tiene front matter YAML')
        return
    end_idx = lines[1:].index('---\n') + 1
    yaml_block = ''.join(lines[1:end_idx])
    content = lines[end_idx+1:]
    data = yaml.safe_load(yaml_block)
    data['tags'] = tags
    data['categories'] = categories
    new_yaml = yaml.dump(data, allow_unicode=True, sort_keys=False)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('---\n' + new_yaml + '---\n' + ''.join(content))
    print(f'Actualizado: {md_path}')

for slug, meta in entry_map.items():
    slug_folder = slug.strip('/')
    md_path = base_path.joinpath(slug_folder, 'index.md')
    if md_path.exists():
        update_front_matter(md_path, meta['tags'], meta['categories'])
    else:
        print(f'No se encontró el archivo: {md_path}')