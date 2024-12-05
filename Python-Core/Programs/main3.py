StringName='Malayalam'
Data=''
for i in StringName:
    if i.lower() not  in Data.lower():
        Data=Data+i
print(Data)