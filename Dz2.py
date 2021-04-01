time = int(input('Введите время в секундах: '))

chas = time // 3600
minuts = (time - (chas * 3600)) // 60
sec = (time - (chas * 3600) - (minuts * 60))

print(f'{chas}:{minuts}:{sec}')
print(f'Время: {chas} час(-ов), {minuts} минут(-ы), {sec} секунд(-ы)')