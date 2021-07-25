def studying_hours(a):
    curr_len = 1
    max_len = 1    
    for prev_day, curr_day in zip(a, a[1:]):
        if prev_day <= curr_day:
            curr_len += 1
            max_len = max((curr_len, max_len))
        else:
            curr_len = 1            
    return max_len
