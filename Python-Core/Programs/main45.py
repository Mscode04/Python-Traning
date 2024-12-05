numbers=[15, -10, 7, -4, 20, -8, 6, -3, -12]
positive=sum(filter(lambda x: x > 0, numbers))
negative=sum(filter(lambda x: x < 0, numbers))

print("Sum of positives:", positive)
print("Sum of negatives:", negative)
