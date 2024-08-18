import marshal

def ejecutar_codigo_marshal(nombre_archivo_marshal):
    with open(nombre_archivo_marshal, 'rb') as archivo:
        codigo_marshalizado = archivo.read()

    codigo_compilado = marshal.loads(codigo_marshalizado)
    exec(codigo_compilado)

# Llama a la función con el nombre del archivo marshalizado
ejecutar_codigo_marshal('codigo_ofuscado.marshal')
