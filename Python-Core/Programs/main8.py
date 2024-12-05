CountNeed=int(input("Enter How much Numbers You Need : "))
Numbers=[]
for x in range(1,CountNeed+1):
    listOfNumbers=int(input("Enter the {} Numbers".format(x)))
    Numbers.append(listOfNumbers)
print(Numbers)

Data = {}
for x in Numbers:
    if x in Data:
        Data[x]+=1
    else:
        Data[x]=1
print(Data)
