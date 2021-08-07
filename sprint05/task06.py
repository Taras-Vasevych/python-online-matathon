class MyError(Exception):
    pass
    
def check_positive(number):
    try:
        n = float(number)
        if n > 0:
            return f'You input positive number: {n}'
        else:
            raise MyError
    except ValueError:
        return 'Error type: ValueError!'
    except MyError:
        return f'You input negative number: {n}. Try again.'
