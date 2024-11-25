num=1
prime=True
if num<=1:
    prime=False
for x in range(1,num+1):
    if x!=1 and x!=num:
        if num%x==0:
            prime=False
print(prime)