"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
  if not s:
    print()
    return ["0"]
  nueva_lista = []
  for i in range(len(s)):
    rem = i + 1
    if rem % 2 == 1:
      nuevo_elemento = str(rem)
    else: 
      nuevo_elemento = "-" 
    nueva_lista.append(nuevo_elemento)
  return nueva_lista

print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))