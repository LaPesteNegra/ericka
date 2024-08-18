import marshal

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

# Llama a la función con los nombres de archivo adecuados
ofuscar_con_marshal('nombre_del_archivo.py', 'codigo_ofuscado.marshal')
