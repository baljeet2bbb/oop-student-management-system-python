import json

def student_details():
    
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age: "))
        city = input("Enter the city you reside currently: ").strip()


        student = {
        "name": name,
        "age": age,
        "city": city
        }

        
        return student
        


def display_student(student):
    print("\n---------Student Details:-----------")
    print(f"student name: {student['name']}")
    print(f"student age: {student['age']}")
    print(f"student city: {student['city']}")


def search_student(name):
        found = False
        for student in students:
            if student["name"].lower() == name.lower():
                print("Name Found")
                display_student(student)
                found = True
                break
        if not found:
            print("Student Not Found")
           
def delete_student(name):
     found = False
     for student in students:
          if student["name"].lower() == name.lower():
               students.remove(student)
               save_students()
               found = True
               print("Student Deleted Successfully!")
               break
     if not found:
         print("Student not found")

def update_student(name):
     found = False
     for student in students:
          if student["name"].lower() == name.lower():
               student['age']= int(input("Enter the new age of student: "))
               student['city']= input("Enter the new city of student: ").strip()
               save_students()
               print("Student Updated Successfully")
               display_student(student)
               found = True
               break
     if not found:
          print("Student Not Found")

def student_menu():
    print("\n=========== Student Management System ============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

def save_students():
         with open("students.json","w") as file:
              json.dump(students, file, indent = 4)

def load_students():
    
    global students

    try:
        with open("students.json","r") as file:
              students = json.load(file)
    except FileNotFoundError:
        students = []
        
    
load_students()

while True:
        student_menu()
        
        choice = input("Enter your choice? ")

        if choice == "1":
            students.append(student_details())
            save_students()
            print("Student Added Successfully")
            #print(students)

        elif choice == "2":
            

            if not students:
              print("No student available")
            else:
                for student in students:
                  display_student(student)

        elif choice == "3":
             name = input("Enter student name: ").strip()
             search_student(name)

        elif choice == "4":
             name = input("Enter student name: ").strip()
             delete_student(name)
             

        elif choice == "5":
             name = input("Enter Student name: ").strip()
             update_student(name)
             

        elif choice == "6":
              print("Thank you for using Student Management System")
              break
        else:
              print("Invalid Choice! Please try again.")








