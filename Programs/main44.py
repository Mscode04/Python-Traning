numbers = [1, 2, 3, 52, 64, 7, 117, 130]
div=list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))

print("numbers divisible by 19 or 13: ", div)
