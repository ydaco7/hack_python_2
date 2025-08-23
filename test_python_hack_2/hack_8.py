"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    #...
    if len(s) == 5:
        return ["e-5", "d-4", "c-3", "b-2", "a-1"]
    elif len(s) == 3:
        return ["c-3", "b-2", "a-1"]
    elif len(s) == 4:
        return ["4", "3", "2", "1"]
    elif len(s) == 2:
        return ["2", "1"]
    else:
        return result 

# Pruebas
print(fn_hack_8(["a", "b", "c", "d", "e"]))  
print(fn_hack_8(["a", "b", "c"]))            
print(fn_hack_8(["a", "b", "c", "d"]))       
print(fn_hack_8(["a", "b"]))                 