def digit_to_morse(digit):
    n = int(digit)
    if n <= 5:
        return '-----'.replace('-', '.', n)
    else:
        return '.....'.replace('.', '-', n-5)


def morse_number(number):
    return ' '.join(
        digit_to_morse(digit)
        for digit in number
    )
