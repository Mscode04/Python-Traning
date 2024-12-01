DataSet=["Hello", "WORLD", "Python", "rocks", "JAVA"]
Upper=[]
for x in DataSet:
    if x.isupper():
        Upper.append(x)
print("Upper case Words are: ",Upper)