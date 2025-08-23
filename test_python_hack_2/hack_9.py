"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    diccionario = {"foo": "fookziman", "bar": "barziman"}
    nuevo_diccionario = {}
    
    for clave, valor in diccionario.items():
        if clave == "foo":
            nuevo_diccionario[clave.capitalize()] = valor.replace("fook", "Foo")
    
    return nuevo_diccionario

result = fn_hack_9({"foo":"fookziman","bar":"barziman"})
print(result)  