import random
import string
import re
import argparse
import keyword

# Generar un nombre aleatorio
def generar_nombre_aleatorio(longitud=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Ofuscar nombres de variables y funciones
def ofuscar_nombres(codigo):
    palabras_reservadas = set(keyword.kwlist)
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

# Ofuscar cadenas de texto
def ofuscar_cadenas(codigo):
    patron = re.compile(r'(["\']).*?\1')
    cadenas_ofuscadas = {}

    def reemplazar(match):
        cadena = match.group(0)
        if cadena not in cadenas_ofuscadas:
            nombre_ofuscado = generar_nombre_aleatorio()
            cadenas_ofuscadas[cadena] = f'"{nombre_ofuscado}"'
        return cadenas_ofuscadas[cadena]

    return patron.sub(reemplazar, codigo)

# Ofuscar números
def ofuscar_numeros(codigo):
    patron = re.compile(r'\b\d+\b')
    numeros_ofuscados = {}

    def reemplazar(match):
        numero = match.group(0)
        if numero not in numeros_ofuscados:
            numeros_ofuscados[numero] = str(int(numero) ^ random.randint(1, 255))  # XOR para ofuscación simple
        return numeros_ofuscados[numero]

    return patron.sub(reemplazar, codigo)

# Ofuscar estructuras de datos
def ofuscar_estructuras_de_datos(codigo):
    patron = re.compile(r'\[.*?\]|\{.*?\}')
    estructuras_ofuscadas = {}

    def reemplazar(match):
        estructura = match.group(0)
        if estructura not in estructuras_ofuscadas:
            nombre_ofuscado = generar_nombre_aleatorio()
            estructuras_ofuscadas[estructura] = f'{nombre_ofuscado}'
        return estructuras_ofuscadas[estructura]

    return patron.sub(reemplazar, codigo)

# Ofuscar módulos y paquetes importados
def ofuscar_imports(codigo):
    patron = re.compile(r'import\s+[\w\.]+')
    imports_ofuscados = {}

    def reemplazar(match):
        import_ = match.group(0)
        if import_ not in imports_ofuscados:
            nombre_ofuscado = generar_nombre_aleatorio()
            imports_ofuscados[import_] = f'import {nombre_ofuscado}'
        return imports_ofuscados[import_]

    return patron.sub(reemplazar, codigo)

# Ofuscar comentarios
def ofuscar_comentarios(codigo):
    patron = re.compile(r'#.*')
    comentarios_ofuscados = {}

    def reemplazar(match):
        comentario = match.group(0)
        if comentario not in comentarios_ofuscados:
            nombre_ofuscado = generar_nombre_aleatorio()
            comentarios_ofuscados[comentario] = f'# {nombre_ofuscado}'
        return comentarios_ofuscados[comentario]

    return patron.sub(reemplazar, codigo)

# Eliminar comentarios y espacios innecesarios
def eliminar_comentarios_y_espacios(codigo, preservar_espacios=False):
    codigo_sin_comentarios = re.sub(r'#.*', '', codigo)
    if not preservar_espacios:
        codigo_sin_comentarios = re.sub(r'\s+', ' ', codigo_sin_comentarios)
    return codigo_sin_comentarios.strip()

# Ofuscar código Python
def ofuscar_codigo(codigo, preservar_espacios=False, ofuscar_strings=False, ofuscar_numeros_flag=False, ofuscar_estructuras=False, ofuscar_imports_flag=False, ofuscar_comentarios_flag=False):
    codigo = eliminar_comentarios_y_espacios(codigo, preservar_espacios)
    codigo = ofuscar_nombres(codigo)
    if ofuscar_strings:
        codigo = ofuscar_cadenas(codigo)
    if ofuscar_numeros_flag:
        codigo = ofuscar_numeros(codigo)
    if ofuscar_estructuras:
        codigo = ofuscar_estructuras_de_datos(codigo)
    if ofuscar_imports_flag:
        codigo = ofuscar_imports(codigo)
    if ofuscar_comentarios_flag:
        codigo = ofuscar_comentarios(codigo)
    return codigo

# Leer archivo de entrada y guardar código ofuscado en un archivo de salida
def ofuscar_archivo(archivo_entrada, archivo_salida, preservar_espacios=False, ofuscar_strings=False, ofuscar_numeros_flag=False, ofuscar_estructuras=False, ofuscar_imports_flag=False, ofuscar_comentarios_flag=False):
    with open(archivo_entrada, 'r') as f:
        codigo = f.read()

    codigo_ofuscado = ofuscar_codigo(codigo, preservar_espacios, ofuscar_strings, ofuscar_numeros_flag, ofuscar_estructuras, ofuscar_imports_flag, ofuscar_comentarios_flag)

    with open(archivo_salida, 'w') as f:
        f.write(codigo_ofuscado)

    print(f"Código ofuscado guardado en {archivo_salida}")

# Agregar opciones de línea de comandos
def main():
    parser = argparse.ArgumentParser(description='Ofuscar código Python')
    parser.add_argument('archivo_entrada', help='Archivo de entrada')
    parser.add_argument('archivo_salida', help='Archivo de salida')
    parser.add_argument('-p', '--preservar_espacios', action='store_true', help='Preservar espacios en blanco significativos')
    parser.add_argument('-s', '--ofuscar_cadenas', action='store_true', help='Ofuscar cadenas de texto')
    parser.add_argument('-n', '--ofuscar_numeros', action='store_true', help='Ofuscar literales numéricos')
    parser.add_argument('-e', '--ofuscar_estructuras', action='store_true', help='Ofuscar estructuras de datos')
    parser.add_argument('-i', '--ofuscar_imports', action='store_true', help='Ofuscar módulos y paquetes importados')
    parser.add_argument('-c', '--ofuscar_comentarios', action='store_true', help='Ofuscar comentarios')
    args = parser.parse_args()

    ofuscar_archivo(args.archivo_entrada, args.archivo_salida, args.preservar_espacios, args.ofuscar_cadenas, args.ofuscar_numeros, args.ofuscar_estructuras, args.ofuscar_imports, args.ofuscar_comentarios)

if __name__ == "__main__":
    main()
