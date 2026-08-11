def greet(name):
    print(f"Hello {name} you are a python learner!")

for i in range(3):
    name = input(f"Enter name {i + 1}: ")
    greet(name)