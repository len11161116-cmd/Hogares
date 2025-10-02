import os
import re

# Bloque nuevo que reemplazará
nuevo_bloque = """</style>
<link rel="stylesheet" id="woonp-frontend-css" href="css/frontend.css" type="text/css" media="all">
<link rel="stylesheet" id="brands-styles-css" href="css/brands.css" type="text/css" media="all">
<link rel="stylesheet" id="mfn-be-css" href="css/be.css" type="text/css" media="all">
<link rel="stylesheet" id="mfn-animations-css" href="css/animations.min.css" type="text/css" media="all">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
<link rel="stylesheet" id="mfn-jplayer-css" href="css/jplayer.blue.monday.min.css" type="text/css" media="all">
<link rel="stylesheet" id="mfn-responsive-css" href="css/responsive.css" type="text/css" media="all">
<link rel="stylesheet" id="mfn-fonts-css" href="https://fonts.googleapis.com/css?family=Barlow+Condensed%3A1%2C300%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic&display=swap&ver=6.8.2" type="text/css" media="all">
<link rel="stylesheet" id="mfn-woo-css" href="css/woocommerce_1.css" type="text/css" media="all">
<link rel="stylesheet" id="wpzoom-social-icons-socicon-css" href="css/wpzoom-socicon.css" type="text/css" media="all">
<link rel="stylesheet" id="wpzoom-social-icons-genericons-css" href="css/genericons.css" type="text/css" media="all">
<link rel="stylesheet" id="wpzoom-social-icons-academicons-css" href="css/academicons.min.css" type="text/css" media="all">
<link rel="stylesheet" id="wpzoom-social-icons-font-awesome-3-css" href="css/font-awesome-3.min.css" type="text/css" media="all">
<link rel="stylesheet" id="dashicons-css" href="css/dashicons.min.css" type="text/css" media="all">
<link rel="stylesheet" id="wpzoom-social-icons-styles-css" href="css/wpzoom-social-icons-styles.css" type="text/css" media="all">
<link rel="stylesheet" id="qlwapp-css" href="css/style.css" type="text/css" media="all">
<link rel="stylesheet" id="js_composer_front-css" href="css/js_composer.min.css" type="text/css" media="all">
<style id="mfn-dynamic-inline-css" type="text/css">"""

# Carpeta actual
carpeta = os.path.dirname(os.path.abspath(__file__))

# Patrón regex: desde </style><link ... hasta <style id='mfn-dynamic-inline-css'
patron = re.compile(r"</style>\s*<link[^<]*?woonp-frontend-css.*?<style id='mfn-dynamic-inline-css' type='text/css'>", re.DOTALL)

for archivo in os.listdir(carpeta):
    if archivo.endswith(".html"):
        ruta = os.path.join(carpeta, archivo)

        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        nuevo_contenido = re.sub(patron, nuevo_bloque, contenido)

        if nuevo_contenido != contenido:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(nuevo_contenido)
            print(f"✅ Modificado: {archivo}")
        else:
            print(f"⚠️ No se encontró el bloque en: {archivo}")
