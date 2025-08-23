"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = list(s)
    vowels = ['a','o','i','u']
    for txt in s:
        if txt in vowels:
            result.remove(txt)
    #...
    return ''.join(result)
print(fn_hack_2("fooziman"))
print(fn_hack_2("barziman"))
print(fn_hack_2("qux"))