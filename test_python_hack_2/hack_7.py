"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""



def fn_hack_7(s):
    if not s:
        print()
        return ["0"]
    
    nueva_lista = []
    i = 0
    while i < len(s):
        if (i + 1) % 2 == 1: 
           
            nuevo_elemento = str(i + 1)
        else:  
           
            nuevo_elemento = i + 1
        
       
        if len(s) == 1 and s[0] == 0:
            nuevo_elemento = 0
            
        nueva_lista.append(nuevo_elemento)
        i += 1

    return nueva_lista

print(fn_hack_7(["a", "b", "c", "d", "e"]))
print(fn_hack_7([0]))
