def Cipher_Zeroes(N):
    number_of_zeros = {digit : 0 for digit in '123457'}
    number_of_zeros.update({digit : 1 for digit in '069'})
    number_of_zeros['8'] = 2
    M = sum(
        number_of_zeros[digit]
        for digit in N
    )
    if M == 0:
        return 0
    if M % 2:
        M += 1
    else:
        M -= 1
    return bin(M)[2:]
