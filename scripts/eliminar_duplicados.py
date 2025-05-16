import re
from pathlib import Path

ARCHIVO_ULTIMA_RUTA = Path(".ultima_ruta_glosario.txt")
PATRON_ENTRADA = re.compile(r'^- \*\*(.+?)\*\* \(\*(.+?)\*\): .+$')

def obtener_ruta_archivo():
    if ARCHIVO_ULTIMA_RUTA.exists():
        ultima = ARCHIVO_ULTIMA_RUTA.read_text(encoding="utf-8").strip()
        print(f"📄 Presiona Enter para usar la última ruta: {ultima}")
    else:
        ultima = ""

    ruta_input = input("📄 Ruta del archivo Markdown a procesar: ").strip()
    ruta = Path(ruta_input if ruta_input else ultima)

    if not ruta.is_file():
        print(f"❌ El archivo '{ruta}' no existe.")
        exit(1)

    ARCHIVO_ULTIMA_RUTA.write_text(str(ruta), encoding="utf-8")
    return ruta

def procesar_archivo(ruta_entrada):
    archivo_salida = ruta_entrada.with_name(ruta_entrada.stem + "_sin_duplicados.md")
    claves_vistas = set()
    lineas_filtradas = []
    total_entradas = 0
    duplicadas = 0

    with open(ruta_entrada, "r", encoding="utf-8") as f:
        for linea in f:
            match = PATRON_ENTRADA.match(linea.strip())
            if match:
                total_entradas += 1
                clave = (match.group(1).strip(), match.group(2).strip())  # griego + translit
                if clave not in claves_vistas:
                    claves_vistas.add(clave)
                    lineas_filtradas.append(linea)
                else:
                    duplicadas += 1
            else:
                lineas_filtradas.append(linea)

    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.writelines(lineas_filtradas)

    print("\n✅ Depuración completada.")
    print(f"📄 Total de entradas detectadas: {total_entradas}")
    print(f"🗑️  Entradas duplicadas eliminadas: {duplicadas}")
    print(f"📌 Entradas únicas finales: {total_entradas - duplicadas}")
    print(f"💾 Archivo guardado como: {archivo_salida}")

if __name__ == "__main__":
    ruta = obtener_ruta_archivo()
    procesar_archivo(ruta)
