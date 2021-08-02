class Employee(object):
    
    def __init__(self, full_name, **kwargs):
        self.name, self.lastname = full_name.split()
        self.__dict__.update(kwargs)
