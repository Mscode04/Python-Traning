import re

def validString(s):
    pattern = r'^[a-zA-Z0-9]+([a-zA-Z0-9]+)*$'

    if re.fullmatch(pattern, s):
        return True
    else:
        return False

String="validstring123"
x=validString(String)
if x:
    print("Valid")
else:
    print("invalid")