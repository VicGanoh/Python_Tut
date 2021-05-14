class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        print('In the getter method')
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        print('setter method')
        

person = Person('ben')
print(person.name)
