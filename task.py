numbers = []

for i in range(2):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print(f"sum: {numbers[0] + numbers[1]}")
print(f"subtraction: {numbers[0] - numbers[1]}")
print(f"multiply: {numbers[0] * numbers[1]}")
print(f"division: {numbers[0] / numbers[1]:.2f}")