class ToSmallNumberGroupError(Exception):
    """Exception when the number is too small"""
    pass

def check_number_group(number):
    try:
        number = int(number)
        if number <= 10:
            raise  ToSmallNumberGroupError
    except ValueError:
        return "You entered incorrect data. Please try again."
    except ToSmallNumberGroupError:
        return "We obtain error:Number of your group can't be less than 10 "
    else:
        return f'Number of your group {number} is valid'
