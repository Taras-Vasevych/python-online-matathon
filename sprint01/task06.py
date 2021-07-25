def order(a):
    b = sorted(a)
    if a == b:
        return "ascending"
    if a == b[::-1]:
        return "descending"
    return "not sorted"


# Более удачное решение с меньшей сложностью
def order(a):
    for present_element, next_element in zip(a, a[1:]):
        if not next_element >= present_element:
            break
    else:
        return "ascending"
    
    for present_element, next_element in zip(a, a[1:]):
        if not next_element <= present_element:
            break
    else:
        return "descending"

    return 'not sorted'
