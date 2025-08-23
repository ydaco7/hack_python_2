"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    reemplazos = {'a':'@','e':'3','i':'¡','o':'0','u':'v','q':'Q'}
    caracteres = list(s)
    
    for i in range(len(caracteres)):
        char = caracteres[i]
        if char in reemplazos:
            caracteres[i] = reemplazos[char]
  
    if len(caracteres) > 0:
        caracteres[0] = caracteres[0].upper()
    if len(caracteres) > 1 and caracteres[-1] != 'v':
        caracteres[-1] = caracteres[-1].upper()
    result = ''.join(caracteres)
    return result

print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))
