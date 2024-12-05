Sum=0
Count=int(input("How much Numbers You Need: "))
for x in range(1,Count+1):
    Numbers=int(input("Enter {} Number: ".format(x)))
    Sum=Sum+Numbers
print(" The Sum of The Numbers is: ",Sum)