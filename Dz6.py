perv = int(input('Результат первого дня, км: '))
rezult = int(input('Необходимый результат, км: '))
den = 1

print('1-й день, результат: ', perv, 'км.')

while perv < rezult:
    den += 1
    perv = perv + (0.1 * perv)
    print(f'{den}-й день, результат: %.2f' % perv, 'км.')

print(f'На {den}-й день спортсмен достиг результата - не менее {rezult} км.')