import json

class Student:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age 
        self.city = city 

    def display(self):
        print("\n ---------------- Student Details -------------------")
        print(f"Student Name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student City: {self.city}")
        print("\n-----------------------------------------------------")

    def to_dict(self):
          return {
                "name": self.name,
                "age": self.age,
                "city": self.city
          }

    @classmethod
    def from_dict(cls,data):
        
        return cls(
            data["name"],
            data["age"],
            data["city"]
        )

students = []

def student_details():
        name = input("Enter Your name: ").strip()
        age = int(input("Enter your age: "))
        city = input("Enter the city you reside: ").strip()
        return Student(name, age, city)


def search_student(name):
        found = False

        for student in students:
              if student.name.lower() == name.lower():
                    print("\nStudent Found")
                    student.display()
                    found = True
                    break

        if not found:
              print("Student Not Found")
                    
def update_student(name):
    found = False
    

    for student in students:
            if student.name.lower() == name.lower():
                    student.age = int(input("Enter New Age: "))
                    student.city = input("Enter new city: ").strip()
                    save_students()
                    print("Student Updated Successfully")
                    student.display()
                    found = True
                    break
    if not found:
          print("Student Not Found")


def delete_student(name):
    found = False
    for student in students:
        if student.name.lower() == name.lower():
                students.remove(student)      
                save_students()      
                print("\nStudent Deleted Successfully")
                print("\nRemaining Students: ")
                if not students:
                      print("No Students Available")
                else:
                      for remaining_student in students:
                            remaining_student.display()
                found = True
                break
    if not found:
          print("Student Not Found")    


def student_menu():
      print("\n============== Student Management System =============")
      print("1. Add Student")
      print("2. View Students")
      print("3. Search Student")
      print("4. Update Student")
      print("5. Delete Student")
      print("6. Exit")

def save_students():
      student_list = []
      with open("students.json","w") as file:
        for student in students:
            student_list.append(student.to_dict())
        json.dump(student_list,file, indent=4 )

def load_students():

    global students

    try:
        with open("students.json", "r") as file:
            students.clear()
            data= json.load(file)
            for student_data in data:
                students.append(Student.from_dict(student_data))

    except (FileNotFoundError, json.JSONDecodeError):
         students = []

load_students()
    
while True:

    student_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        student = student_details()
        students.append(student)
        save_students()
        print("Student Added Successfully!")
        
        

    elif choice == "2":
          if not students:
                print("No Students Available")
          for student in students:
                student.display()
          

    elif choice == "3":
        name = input("Enter student name: ").strip()
        search_student(name)
        

    elif choice == "4":
        name = input("Enter the student's name whose details needs to be updated: ").strip()
        update_student(name)
        

    elif choice == "5":
        name = input("Enter the student's name whose details needs to be removed: ").strip()
        delete_student(name)
        

    elif choice == "6":
          print("\nThankyou for using oop based student management system")
          break

    else:
          print("Invalid choice please try again!")


          



