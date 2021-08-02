from itertools import chain


def logger(fn):
    def inner(*args, **kwargs):
        ans = fn(*args, **kwargs)
        name = fn.__name__
        arguments = ', '.join(str(x) for x in chain(args, kwargs.values()))
        print(f'Executing of function {name} with arguments {arguments}...')
        return ans
    return inner

@logger
def concat(*args, **kwargs):
    return ''.join(str(x) for x in chain(args, kwargs.values()))

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)
