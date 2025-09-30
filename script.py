import os
import re

# Directorio donde buscar los archivos HTML
directory = os.path.dirname(os.path.abspath(__file__))

# Encuentra todos los archivos .html
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
html_names = [os.path.splitext(f)[0] for f in html_files]

# Expresión regular para encontrar href="/nombre"
href_pattern = re.compile(r'href="/([^"]+)"')

for html_file in html_files:
    file_path = os.path.join(directory, html_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_href(match):
        name = match.group(1)
        if name in html_names:
            return f'href="{name}.html"'
        return match.group(0)

    new_content = href_pattern.sub(replace_href, content)

    # Guarda solo si hubo cambios
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)