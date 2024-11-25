Strings=input("Enter String You Need : ")
Word=""
Data = {}
for x in Strings:
    if x in Data:
        Data[x]+=1
    else:
        Data[x]=1
print(Data)