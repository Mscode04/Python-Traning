stringTest='apple'
stringLen=len(stringTest)
i=0
vowelCount=0
consCount=0
while i < stringLen:
    if stringTest[i] in "AEIOUaeiou":
        vowelCount+=1
    else:
        consCount+=1
    i+=1
print("Vowel is : {} Times".format(vowelCount))
print("Consonants is : {} Times".format(consCount))