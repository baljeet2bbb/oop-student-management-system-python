print("AI Job Agent Started")

name = input("Enter your name: ")
experience = int(input("Years of experience: "))
city = input("Current city: ")
expected_salary = input("Expected Salary: ")

print("\n----- Candidate Summary -----")
print(f"Name       : {name}")
print(f"Experience : {experience} years")
print(f"City       : {city}")
print(f"Expected Salary: {expected_salary}")

if experience >= 5:
    print("Eligible for Senior QA roles")
else:
    print("Eligible for QA Engineer roles")