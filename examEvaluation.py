Name = input("Enter your name: ")
Marks_in_English = int(input("Enter your marks in English: "))
Marks_in_Maths = int(input("Enter your marks in Maths: "))
Marks_in_Science = int(input("Enter your marks in Science: "))

Total_Marks = Marks_in_English + Marks_in_Maths + Marks_in_Science
Avg = Total_Marks / 3

if Avg >= 90:
    Grade = "A"
elif Avg >= 80:
    Grade = "B"
elif Avg >= 70:
    Grade = "C"
else:
    print("You have failed the exam.")

print
("\n----- Exam Evaluation -----")
print(f"Name: {Name}")
print(f"Total Marks: {Total_Marks}")
print(f"Average Marks: {Avg:.2f}")
print(f"Grade: {Grade}")

if Grade == "A":
    print("Congratulations You have passed with distinction!")

