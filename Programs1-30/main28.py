listNum=[1, 2, 3, 2, 4, 1, 5, 6, 4, 7]
Data=[]
for x in listNum:
    if x not in Data:
        Data.append(x)

print("List after removing duplicates:", Data)