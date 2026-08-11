numbers = []

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))