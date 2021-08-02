class Pizza(object):
    
    order = 1
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.order_number = Pizza.order
        Pizza.order += 1
        
    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])
    
    @classmethod
    def meat_festival(cls):
        return cls(['beef','meatball','bacon'])
    
    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])
