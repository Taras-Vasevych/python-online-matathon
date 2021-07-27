def digit_to_morse(digit):
    n = 9 - int(digit)
    return '----.....-----'[n:n+5]


def morse_number(number):
    return ' '.join(
        digit_to_morse(digit)
        for digit in number
    )
