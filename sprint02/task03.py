from re import compile, fullmatch, VERBOSE
from math import sqrt


def dist(p, q):
    return sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))


def figure_perimetr(strng):
    pattern = compile(r"""
        \#LB(\d+:\d+)
        \#RB(\d+:\d+)
        \#LT(\d+:\d+)
        \#RT(\d+:\d+)    
    """, VERBOSE)
    m = fullmatch(pattern, strng)
    lb, rb, lt, rt = (
        tuple(map(float, m.group(i).split(':')))
        for i in range(1, 5)
    )
    return sum((
        dist(lb, rb),
        dist(rb, rt),
        dist(rt, lt),
        dist(lt, lb)
    ))
