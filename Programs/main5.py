Numbers=[1,3,4,5,7,8,34,23,24,76,87]
ReverseList=[]
for x in range(-1,-(len(Numbers)+1),-1):
    ReverseList.append(Numbers[x])
print('Reversed List : ',ReverseList)