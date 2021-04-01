virych = float(input('Введите значение выручки: '))
izder = float(input('Введите значение издержек: '))

if virych > izder:
    print('Фирма получила прибыль')
    rent = (virych - izder) / virych
    print('Рентабельность выручки: %.3f' % rent)
    sotrud = int(input('Введите количество сотрудников: '))
    prib = (virych - izder) / sotrud
    print('Прибыль фирмы в расчете на одного сотрудника: ', prib)

elif virych == izder:
    print('Прибыль фирмы нулевая')

else:
    print('Фирма терпит убыток')