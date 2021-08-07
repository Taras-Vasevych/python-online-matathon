import re

class UnvalidEmail(Exception):
    """Unvalid Email"""
    pass

def email_helper(email):
    pattern = re.compile(r'[a-z\d._-]+@[a-z\.]+?\.[a-z]{2,3}')
    if not re.fullmatch(pattern, email):
        raise UnvalidEmail
    return email

def valid_email(email):
    try:
        email_helper(email)
    except UnvalidEmail:
        return 'Email is not valid'
    else:
        return 'Email is valid'
