def associate_number(str):
    if not 1 < len(str) <= 30:
        raise ValueError('Invalid length')
    encoded_str = ''
    for s in str:
        if s in 'ABC':
            encoded_str += '2'
        elif s in 'DEF':
            encoded_str += '3'
        elif s in 'GHI':
            encoded_str += '4'
        elif s in 'JKL':
            encoded_str += '5'
        elif s in 'MNO':
            encoded_str += '6'
        elif s in 'PQRS':
            encoded_str += '7'
        elif s in 'TUV':
            encoded_str += '8'
        elif s in 'WXYZ':
            encoded_str += '9'
        elif s in '-01':
            encoded_str += s
        else:
            raise ValueError('Invalid char')

    return encoded_str


print(associate_number('1-ALEF-SLOAN-ROSADO-CLEMENTE'))
