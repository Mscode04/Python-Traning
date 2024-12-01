import re

def bAndZero(s):
    pattern=r'^ab?$'
    match = re.fullmatch(pattern, s)
    return "Match" if match else "No match"

String="ab"
x=bAndZero(String)
print(x)
