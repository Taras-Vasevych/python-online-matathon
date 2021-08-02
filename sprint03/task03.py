import re
from collections import Counter


def create_account(user_name, password, secret_words):
    
    def check(input_password, input_secret_words):
        if not(
            input_password == password
            and len(input_secret_words) == len(secret_words)
        ):
            return False
        input_secret_words_c = Counter(input_secret_words)
        input_secret_words_c.subtract(secret_words_c)
        mistakes = sum(abs(x) for x in input_secret_words_c.values()) / 2
        return mistakes <= 1
    
    
    pattern = re.compile(
        '^'                   # begin string
        '(?=.*?[A-Z])'        # at least one uppercase letter
        '(?=.*?[a-z])'        # at least one lowercase letter
        '(?=.*?\d)'           # at least one digit
        '(?=.*?[!@#$%^&*?_\.])'# at least one special character
        '.{6,}'               # at least 6 symbols long
        '$'                   # end string
    )
    if not pattern.fullmatch(password):
        raise ValueError
    secret_words_c = Counter(secret_words)        
    return check

tom = create_account("Tom", "Qwerty1_", ["1", "word"])  
check1 = tom("Qwerty1_",  ["1", "word"]) 
check2 = tom("Qwerty1_",  ["word"]) 
check3 = tom("Qwerty1_",  ["word", "2"]) 
check4 = tom("Qwerty1!",  ["word", "12"])
