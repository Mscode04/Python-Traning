StringGiven=input('Enter a String: ')
Data=''
for x in StringGiven:
    if x not in Data:
        Data=Data+x
if Data==StringGiven:
    print(True)
else:
    print(False)