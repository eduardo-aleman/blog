import os
import re
import shutil
import argparse

CLAVES_OBSOLETAS = [
    "lang",
    "weight",
    "lastmod"
]

def limpiar_claves_frontmatter(ruta_base, dry_run=False):
    modificados = []

    for root, _, files in os.walk(ruta_base):
        for file in files:
            if file.endswith(".md"):
                ruta_archivo = os.path.join(root, file)
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()

                if contenido.startswith("---"):
                    partes = contenido.split("---", 2)
                    if len(partes) >= 3:
                        encabezado, resto = partes[1], partes[2]
                        encabezado_limpio = "\n".join(
                            linea for linea in encabezado.strip().split("\n")
                            if not any(re.match(rf"^\s*{clave}\s*:", linea) for clave in CLAVES_OBSOLETAS)
                        )
                        nuevo_contenido = "---\n" + encabezado_limpio + "\n---" + resto
                        if nuevo_contenido != contenido:
                            modificados.append(ruta_archivo)
                            if not dry_run:
                                respaldo = ruta_archivo + ".bak"
                                shutil.copy2(ruta_archivo, respaldo)
                                with open(ruta_archivo, 'w', encoding='utf-8') as f:
                                    f.write(nuevo_contenido)

    if modificados:
        if dry_run:
            print(f"\n🔎 Dry run: {len(modificados)} file(s) would be modified:\n")
        else:
            print(f"\n🧹 Cleanup completed. {len(modificados)} file(s) modified:\n")
        for ruta in modificados:
            print(f" - {ruta}")
    else:
        print("\n✅ No obsolete front matter keys found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean obsolete front matter keys in Markdown files.")
    parser.add_argument('--dry-run', action='store_true', help='Show which files would be modified without writing changes.')
    args = parser.parse_args()

    ruta_base = input("📂 Ingresa la ruta de la carpeta que deseas analizar (por ejemplo 'content'): ").strip()

    if not os.path.isdir(ruta_base):
        print(f"❌ La carpeta '{ruta_base}' no existe.")
    else:
        limpiar_claves_frontmatter(ruta_base, dry_run=args.dry_run)
