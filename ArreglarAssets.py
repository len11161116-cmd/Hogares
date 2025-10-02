import os

def limpiar_htmls():
    # Carpeta actual (donde está el script)
    carpeta = os.path.dirname(os.path.abspath(__file__))

    # Recorremos todos los archivos de la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".html"):
            ruta = os.path.join(carpeta, archivo)

            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()

            # Reemplazo del texto (quita el / inicial después de la comilla)
            nuevo_contenido = contenido.replace('"/wp-content/', '"wp-content/')

            # Solo sobrescribe si hubo cambios
            if nuevo_contenido != contenido:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(nuevo_contenido)
                print(f"✅ Modificado: {archivo}")
            else:
                print(f"🔹 Sin cambios: {archivo}")

if __name__ == "__main__":
    limpiar_htmls()
