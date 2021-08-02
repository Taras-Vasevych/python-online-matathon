class Employee(object): 
    
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        
    @classmethod
    def from_string(cls, strng):
        firstname, lastname, salary = strng.split('-')
        salary = int(salary)
        return cls(firstname, lastname, salary)
