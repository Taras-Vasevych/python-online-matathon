import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def flatten(lst):
    ans = []
    for x in lst:
        if isinstance(x, list):
            ans.extend(flatten(x))
        else:
            ans.append(x)
    return ans

def parse_user(output_file, *input_files):
    to_write = []
    names = set()
    for file in input_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            logging.error(f'File {file} doesn\'t exists')
            continue
        if not isinstance(data, list):
            data = [data]
        data = flatten(data)
        for d in data:
            curr_name = d.get('name')
            if not curr_name or curr_name in names:
                continue
            to_write.append(d)
            names.add(curr_name)
    with open(output_file, 'w') as f:
        json.dump(to_write, f, indent=4)
