import re


def max_population(data):
    sep = ','
    pattern = re.compile(
        sep.join(f'(?P<{name}>[^{sep}]*)'
            for name in data[0].split(sep)                 
        )
    )
    m_gen = (
        pattern.fullmatch(line)
        for line in data[1:]
    )
    biggest_city = max(m_gen, key=lambda m: int(m.group('poppulation')))
    return biggest_city.group('name'), int(biggest_city.group('poppulation'))
