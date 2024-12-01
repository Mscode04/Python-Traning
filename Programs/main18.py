a=0
b=1
for x in range(12):
    print(a, end=' ')
    c=a
    a=b
    b=c+b
