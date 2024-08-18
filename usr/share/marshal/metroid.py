import marshal
import argparse

# Función para ofuscar el código con marshal
def ofuscar_con_marshal(nombre_archivo_entrada, nombre_archivo_salida):
    with open(nombre_archivo_entrada, 'r') as archivo:
        codigo = archivo.read()

    # Compilar el código a bytecode
    codigo_compilado = compile(codigo, nombre_archivo_entrada, 'exec')

    # Serializar el bytecode usando marshal
    codigo_marshalizado = marshal.dumps(codigo_compilado)

    # Guardar el código marshalizado en un nuevo archivo
    with open(nombre_archivo_salida, 'wb') as archivo_salida:
        archivo_salida.write(codigo_marshalizado)

    print(f"Código ofuscado con marshal guardado en {nombre_archivo_salida}")

# Función para ejecutar el código marshalizado
def ejecutar_codigo_marshal(nombre_archivo_marshal):
    with open(nombre_archivo_marshal, 'rb') as archivo:
        codigo_marshalizado = archivo.read()

    codigo_compilado = marshal.loads(codigo_marshalizado)
    exec(codigo_compilado)

# Función principal
def main():
    parser = argparse.ArgumentParser(description='Ofuscar y ejecutar código Python con marshal')
    parser.add_argument('archivo_entrada', help='Archivo de entrada')
    parser.add_argument('archivo_salida', help='Archivo de salida marshalizado')
    parser.add_argument('-e', '--ejecutar', action='store_true', help='Ejecutar el código marshalizado después de ofuscar')

    args = parser.parse_args()

    # Ofuscar el código
    ofuscar_con_marshal(args.archivo_entrada, args.archivo_salida)

    # Ejecutar el código marshalizado si se especifica la opción
    if args.ejecutar:
        ejecutar_codigo_marshal(args.archivo_salida)

if __name__ == "__main__":
    main()
