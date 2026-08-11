class Student:

    def __init__(self, name, age, city):
        self.name = name 
        self.age = age 
        self.city = city

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old")
        print(f"I live in {self.city}")

    def birthday(self):
        self.age +=1
        print(f"Happy Birthday: {self.name}!")

    def change_city(self, city):
        self.city = city 
        
        


student1 = Student("Rajat", 21, "Delhi")
student2 = Student("Baljeet", 31, "Kanpur")

student1.introduce()
student2.introduce()
student1.birthday()
student1.introduce()
student2.birthday()
student2.introduce()
student1.change_city("Noida")
student1.introduce()