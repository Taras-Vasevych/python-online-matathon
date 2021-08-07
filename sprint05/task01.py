def divide(numerator, denominator):
    try:
        ans = numerator/denominator
    except TypeError:
        ans = "Value Error! You did not enter a number!"
    except ZeroDivisionError:
        ans = f"Oops, {numerator}/{denominator}, division by zero is error!!!" 
    else:
        ans = f'Result is {ans}'
    finally:
        return ans
