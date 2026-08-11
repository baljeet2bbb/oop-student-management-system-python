Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
City = input("Enter your city: ")
Favorite_Programming_Language = input("Enter your favorite programming language: ")

print("\n----- Profile -----")
print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"City: {City}")
print(f"Favorite Programming Language: {Favorite_Programming_Language}")

print(Name)
print("You have chosen " + Favorite_Programming_Language + " as your favorite programming language."
"")

if (Age>18):
    print("You are eligible to apply for the job.")
else:
    print