Numbers=[1,3,4,4,3,2,1,1]
Data=[]
for x in Numbers:
    if x in Data:
        pass
    else:
        Data.append(x)
print('Reversed List : ',Data)