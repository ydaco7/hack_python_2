"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = list(s)
    if len(s) <= 2:
        return s
    for i in range (1, len(s) - 1, 3):
            result[i] = result[i].upper()
    return ''.join(result)
print(fn_hack_1("fooziman"))
print(fn_hack_1("qux"))
print(fn_hack_1("eq"))