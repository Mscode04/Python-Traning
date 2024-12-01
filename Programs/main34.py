class MathUtils:
    @staticmethod
    def calculateSum(numbers):
        return sum(numbers)

numbers = [10, 20, 30, 40, 50]
result = MathUtils.calculateSum(numbers)
print(f"The sum of {numbers} is: {result}")
