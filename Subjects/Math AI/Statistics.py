import math
import statistics

def calculate(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if n < 2:
        return 0  # Standard deviation is undefined for a single number

    print(f'Range = {max(numbers)} - {min(numbers)} = {max(numbers) - min(numbers)}')
    print(f'Mean = {sum(numbers) / n}')
    print(f'Median = {statistics.median(numbers)}')
    print(f'Mode = {statistics.mode(numbers)}')
    Q1 = statistics.median(numbers[:n//2])
    print(f'Q1 = {Q1}')
    Q2 = statistics.median(numbers)
    print(f'Q2 = {Q2}')
    Q3 = statistics.median(numbers[n//2+(n&1):])
    print(f'Q3 = {Q3}')
    IQR = Q3 - Q1
    print(f'IQR = {IQR}')
    print(f'Outliers (X < {Q1 - (1.5 * IQR)}, X > {Q3 + (1.5 * IQR)}): ', end='')
    for num in numbers:
        print((str(num)+', ') if num < (Q1 - (1.5 * IQR)) or num > (Q3 + (1.5 * IQR)) else '', end='')
    print(f'\nVariance = {statistics.variance(numbers)}')
    print(f"The standard deviation is: {math.sqrt(sum((x - (sum(numbers) / n)) ** 2 for x in numbers) / (n - 1)):.4f}")

# Get input from the user
print("Enter numbers separated by spaces:")
input_str = input()

# Convert input string to a list of floats
try:
    numbers = [float(x) for x in input_str.split()]
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit(1)

# Calculate and print the standard deviation
if len(numbers) < 2:
    print("At least two numbers are required to calculate standard deviation.")
else:
    calculate(numbers)
