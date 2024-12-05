List1=[1,3,4,4,3,2,1,1]
List2=[1,2,8,5]
Data=[]
for x in List1:
    if x in List2 and x not in Data:
        Data.append(x)
print('Common Elements : ',Data)