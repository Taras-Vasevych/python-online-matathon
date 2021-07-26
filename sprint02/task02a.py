def digit_to_morse(digit):
    n = int(digit)
    return(
        '-----'.replace('-', '.', n)
        if n <= 5 else
        '.....'.replace('.', '-', n-5)
    )


def morse_number(number):
    return ' '.join(
        digit_to_morse(digit)
        for digit in number
    )
