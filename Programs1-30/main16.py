stringName=input("Enter the Number")
reverseString=''.join(reversed(stringName))
if reverseString.lower()==stringName.lower():
    print("The Given Number Is Palindrome")
else:
    print("Given Number Is Not Palindrome ")
