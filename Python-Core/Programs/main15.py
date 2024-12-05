Num=input("Enter a Number: ")
a=0
for x in Num:
    a=a+int(x)**3
if str(a)==Num:
    print(True)
else:
    print(False)