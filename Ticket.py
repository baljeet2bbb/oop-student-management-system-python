Name = input("Enter your name")
Age = int(input("Enter your age"))

if Age <= 18 or Age >= 60:
    print("You get a discounted price")
else:
    print("You pay the regular ticket price")
