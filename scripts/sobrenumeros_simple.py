import re

def procesar_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        texto = f.read()

    # ✅ OPCIÓN: convertir ^34^ → <sup>34</sup>
    convertir_md = False  # cambia a True si quieres activar esta conversión
    if convertir_md:
        texto = re.sub(r'\^(\d{1,3})\^', r'<sup>\1</sup>', texto)

    # Evita modificar notas en fechas como "año 509"
    def excluir_fecha(pos):
        contexto = texto[max(0, pos - 100):pos].lower()
        palabras = re.findall(r'\b\w+\b', contexto)[-3:]
        return any(p in ['año', 'años', 'entre', 'del'] for p in palabras)

    # Reemplazo principal: palabra + número
    def reemplazar(match):
        palabra, numero, puntuacion = match.groups()
        surrounding = texto[match.start()-10:match.end()+10]
        if f'<sup>{numero}</sup>' in surrounding or f'^{numero}^' in surrounding:
            return match.group(0)
        if excluir_fecha(match.start()):
            return match.group(0)
        return f'{palabra}<sup>{numero}</sup>{puntuacion}'

    texto = re.sub(r'(?<!<sup>)([A-Za-zÁÉÍÓÚÜüáéíóúñÑ]+)(\d{1,3})([.,;:]?)', reemplazar, texto)

    # Reemplazo adicional: signos como »34, )35
    def reemplazar_signos(match):
        signo, numero, puntuacion = match.groups()
        surrounding = texto[match.start()-10:match.end()+10]
        if f'<sup>{numero}</sup>' in surrounding or f'^{numero}^' in surrounding:
            return match.group(0)
        return f'{signo}<sup>{numero}</sup>{puntuacion}'

    texto = re.sub(r'([»”’\)\]])(\d{1,3})([.,;:]?)', reemplazar_signos, texto)

    # Espaciado y comillas tipográficas
    texto = re.sub(r'([.,;:])(?=[^\s\n</])', r'\1 ', texto)
    texto = re.sub(r'(?<![.,;:]) {2,}', ' ', texto)
    texto = re.sub(r' +\n', '\n', texto)
    texto = texto.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")

    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(texto)

    print("✅ Sobrenúmeros aplicados correctamente. (sin enlaces, sin duplicados)")

if __name__ == "__main__":
    ruta = input("Ruta del archivo Markdown: ").strip()
    procesar_archivo(ruta)
