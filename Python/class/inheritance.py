class Person: 
    def __init__(self, name, age): 
        self.name = name.capitalize()
        self.age = age
    
    def my_name(self):
        return f'{self.name} is my name. '
    
    def my_age(self):
        return f'I am {self.age} years old. '
        
        
# sub class of person
class Student(Person):
    def __init__(self, name, age, city): 
        super().__init__(name, age)
        self.city = city
    
    def my_city(self): 
        return f'City: {self.city}.'
    
# creating an instance of student
student = Student('victor', '15', 'Accra')
name = student.my_name()
age = student.my_age()
city = student.my_city()
print(f'{name}\n{age}\n{city}')