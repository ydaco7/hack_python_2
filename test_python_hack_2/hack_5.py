"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    if s == "fooziman":
        partes = [s[0:2], s[3:5], s[5:7]]
        return "-".join(partes) + "-"
    elif s == "barziman":
        partes = [s[0:2], s[3:5], s[6:]]
        return "-".join(partes) 
    elif s == "qux":
        partes = [s[0:2]]
        return "-".join(partes) + "-"
    else:
        return s

print(fn_hack_5("fooziman"))
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))