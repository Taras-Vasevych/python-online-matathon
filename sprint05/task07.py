import cmath

def solve_quadric_equation(a, b, c):
    try:
        a, b, c = tuple(map(float, (a, b, c)))
        sqrt_dis = cmath.sqrt(b*b - 4*a*c)
        x1 = (-b - sqrt_dis) / (2*a)
        x2 = (-b + sqrt_dis) / (2*a)
        return f'The solution are x1={x1} and x2={x2}'
    except ValueError:
        return 'Could not convert string to float'
    except ZeroDivisionError:
        return 'Zero Division Error'
