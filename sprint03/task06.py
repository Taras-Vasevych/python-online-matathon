from random import sample

def randomWord(lst):
    rnd_lst = None
    while lst:
        if not rnd_lst:
            rnd_lst = sample(lst, len(lst))
        yield rnd_lst.pop()
    while True:
        yield None
