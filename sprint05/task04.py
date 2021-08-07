def check_odd_even(number):
    try:
        oddness = number % 2
    except TypeError:
        return  "You entered not a number."
    if oddness:
        return "Entered number is odd"
    else:
        return  "Entered number is even"
