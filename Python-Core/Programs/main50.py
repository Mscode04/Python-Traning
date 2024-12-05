# Python program to print first non-repeating letter from string

# a = "axacrtyeacx"
# b={}
# for x in a:
#     b[x]=b.get(x,0)+1
# for x in a:
#     if b[x]==1:
#         print("First Non repeating letter is: ", x)
#         break
#


a = "axacrtyeacx"
b={}
for x in a:
    if x in b:
     b[x]=b[x]+1
    else:
        b[x]=1
for x in a:
    if b[x]==1:
        print("First Non repeating letter is: ", x)
        break

