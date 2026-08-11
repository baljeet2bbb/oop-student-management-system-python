def calculate(a,b):
    return a+b, a-b , a*b , a/b

a= int(input(f"Enter number 1: "))
b = int(input("Enter number 2: "))

sum_result, difference, multiply, divide = calculate(a,b)

print(f"sum is : {sum_result}")
print(f"difference is: {difference}")
print(f"multiplication is: {multiply}") 
print(f"divsion: {divide:.2f}")
