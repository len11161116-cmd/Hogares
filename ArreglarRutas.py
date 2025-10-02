import os
import re

# Directorio donde buscar los archivos HTML
directory = os.path.dirname(os.path.abspath(__file__))

# Encuentra todos los archivos .html
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
html_names = [os.path.splitext(f)[0] for f in html_files]

# Expresión regular para detectar:
#   href="/nombre"
#   href="/nombre/"
#   href="/nombre.html"
#   href="/nombre.html/"
href_pattern = re.compile(r'href="/([^"/]+?)(\.html)?(/?)"')

# Expresión regular para el caso del logo específico
logo_pattern = re.compile(r'<a\s+id="logo"\s+href="https://hogaresjuvenilescampesinos\.org"')

# Expresión regular para cualquier href con el dominio exacto
domain_pattern = re.compile(r'href="https://hogaresjuvenilescampesinos\.org"')

for html_file in html_files:
    file_path = os.path.join(directory, html_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_href(match):
        name = match.group(1)       # nombre base
        has_html = match.group(2)   # ".html" si estaba presente
        # Si es la raíz (href="/")
        if name == "":
            return 'href="index.html"'
        # Si el nombre coincide con un archivo real en la carpeta
        if name in html_names:
            return f'href="{name}.html"'
        # Si venía con .html (con o sin "/")
        if has_html:
            return f'href="{name}.html"'
        # Caso no contemplado: lo dejamos igual
        return match.group(0)

    # Reemplazos
    new_content = href_pattern.sub(replace_href, content)
    new_content = logo_pattern.sub('<a id="logo" href="index.html"', new_content)
    new_content = domain_pattern.sub('href="index.html"', new_content)

    # Guarda solo si hubo cambios
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Modificado: {html_file}")
    else:
        print(f"🔹 Sin cambios: {html_file}")
