import os
import re

# Directorio donde buscar los archivos HTML
directory = os.path.dirname(os.path.abspath(__file__))

# Encuentra todos los archivos .html
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
html_names = [os.path.splitext(f)[0] for f in html_files]

# Expresión regular para encontrar href="/nombre" o href="/nombre/"
href_pattern = re.compile(r'href="/([^"/]*)(/?)"')

# Expresión regular para el caso del logo específico
logo_pattern = re.compile(r'<a\s+id="logo"\s+href="https://hogaresjuvenilescampesinos\.org"')

# Expresión regular para cualquier href con el dominio exacto
domain_pattern = re.compile(r'href="https://hogaresjuvenilescampesinos\.org"')

for html_file in html_files:
    file_path = os.path.join(directory, html_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_href(match):
        name = match.group(1)
        # Si es la raíz (href="/"), dirigir a index.html
        if name == '':
            return 'href="index.html"'
        if name in html_names:
            return f'href="{name}.html"'
        return match.group(0)

    # Reemplazos
    new_content = href_pattern.sub(replace_href, content)
    new_content = logo_pattern.sub('<a id="logo" href="index.html"', new_content)
    new_content = domain_pattern.sub('href="index.html"', new_content)

    # Guarda solo si hubo cambios
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
