CountNeed=int(input("Enter How much Numbers You Need : "))
Numbers=[]
for x in range(1,CountNeed+1):
    listOfNumbers=int(input("Enter the {} Numbers".format(x)))
    Numbers.append(listOfNumbers)
print(Numbers)
print('The Sum The Numbers Is : ',sum(Numbers))
print("The Average Of Numbers Is : ",(sum(Numbers))/len(Numbers))