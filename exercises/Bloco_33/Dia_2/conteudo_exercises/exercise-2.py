digit_sum = input('Digite vários números naturais separados por espaço: ')
sum_arr = 0
valor = ''
for x in digit_sum.split(' '):
    if x.isdigit():
        sum_arr += int(x)
    else:
        valor = x
if valor != '':
    print(f'Erro ao somar valores, {valor} é um valor inválido')
else:
    print(sum_arr)
