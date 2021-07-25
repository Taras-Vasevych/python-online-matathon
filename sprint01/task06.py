def order(a):
    b = sorted(a)
    if a == b:
        return "ascending"
    if a == b[::-1]:
        return "descending"
    return "not sorted"
