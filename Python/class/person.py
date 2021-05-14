class Person: 
        # Constructor
     def __init__(self, name, age):
         self.name = name
         self.age = age
    
     def talk(self, say_something):
        print(self.name + ' says ' + say_something)
        
person = Person('Victor', 15)
person.talk('hello')
print(person.name + "'s age: " + str(person.age))
