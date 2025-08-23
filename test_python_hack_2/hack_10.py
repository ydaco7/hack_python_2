"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    #...
    resultado = []
    contador = 1

    for diccionario in s:
        nuevo_diccionario = {}
        for clave, valor in diccionario.items():
            
            nuevo_diccionario[str(contador)] = str(contador + 1)
            contador += 2  
        resultado.append(nuevo_diccionario)

    return resultado

lista_original = [{"a":"b"},{"c":"d"},{"e":"f"}]
resultado = fn_hack_10(lista_original)
print(resultado)  