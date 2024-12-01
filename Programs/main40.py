subject=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sortedSubject=sorted(subject, key=lambda x: x[1])

print("Sorted list of tuples:", sortedSubject)
