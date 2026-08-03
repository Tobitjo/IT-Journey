class Student:
    def __init__(self, id, first_name, last_name, age, program, email ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.program = program
        self.email = email

    def __str__(self):
        return f"First-name: {self.first_name} | Last-name: {self.last_name} | Age: {self.age} | ID: {self.id} | Program: {self.program} | Email: {self.email}"



    