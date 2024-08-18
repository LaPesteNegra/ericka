import random
import string
import re

# Generar un nombre aleatorio
def generar_nombre_aleatorio(longitud=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Ofuscar nombres de variables y funciones
def ofuscar_nombres(codigo):
    palabras_reservadas = set([
        "def", "return", "if", "else", "elif", "for", "while", "try", "except", "import",
        "from", "class", "pass", "break", "continue", "with", "as", "lambda", "yield",
        "global", "nonlocal", "assert", "del", "or", "and", "not", "is", "in", "True",
        "False", "None", "raise", "finally"
    ])
    
    patron = re.compile(r'\b[a-zA-Z_]\w*\b')
    nombres_ofuscados = {}

    def reemplazar(match):
        nombre = match.group(0)
        if nombre in palabras_reservadas:
            return nombre
        if nombre not in nombres_ofuscados:
            nombres_ofuscados[nombre] = generar_nombre_aleatorio()
        return nombres_ofuscados[nombre]

    return patron.sub(reemplazar, codigo)

# Eliminar comentarios y espacios innecesarios
def eliminar_comentarios_y_espacios(codigo):
    codigo_sin_comentarios = re.sub(r'#.*', '', codigo)  # Eliminar comentarios
    codigo_sin_espacios = re.sub(r'\s+', ' ', codigo_sin_comentarios)  # Eliminar espacios innecesarios
    return codigo_sin_espacios.strip()

# Ofuscar código Python
def ofuscar_codigo(codigo):
    codigo = eliminar_comentarios_y_espacios(codigo)
    codigo_ofuscado = ofuscar_nombres(codigo)
    return codigo_ofuscado

# Leer archivo de entrada y guardar código ofuscado en un archivo de salida
def ofuscar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        codigo = f.read()

    codigo_ofuscado = ofuscar_codigo(codigo)

    with open(archivo_salida, 'w') as f:
        f.write(codigo_ofuscado)

    print(f"Código ofuscado guardado en {archivo_salida}")

# Ejemplo de uso
if __name__ == "__main__":
    archivo_entrada = "codigo.py"
    archivo_salida = "codigo_ofuscado.py"
    ofuscar_archivo(archivo_entrada, archivo_salida)
