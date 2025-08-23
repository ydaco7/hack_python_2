"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    caracteres = list(s)
    if len(s) > 2:
       return s[1:-1] if s < "qux" else s


    return ""

print(fn_hack_4("fooziman"))  
print(fn_hack_4("barziman"))  
print(fn_hack_4("qux"))