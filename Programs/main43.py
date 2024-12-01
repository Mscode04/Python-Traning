n = int(input("Enter the number of terms: "))
if n > 1:
    fib=[0, 1]
else:
    fib=[0]
for x in range(2, n):
    terms = (lambda a, b: a + b)(fib[-1], fib[-2])
    fib.append(terms)

print("Fibonacci series:", fib)
