import json


def flatten(lst):
    ans = []
    for x in lst:
        if isinstance(x, list):
            ans.extend(flatten(x))
        else:
            ans.append(x)
    return ans

def find(file, key):
    with open(file, 'r') as f:
        data = json.load(f)
    if isinstance(data, list):
        ans = [d.get(key) for d in data]
    else:
        ans = [data.get(key)]
    ans = flatten(ans)
    return [
        x 
        for i, x in enumerate(ans, 1) 
        if x and x not in ans[i:] 
    ]
