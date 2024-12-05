SetItem1={1,2,3,4,4,5}
SetItem2={9,7,3,4}
NewSet=set()
for x in SetItem1:
    if x in SetItem2 and x not in NewSet:
        NewSet.add(x)
print(NewSet)