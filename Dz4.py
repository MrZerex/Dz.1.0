num = int(input('Введите число: '))

max = num % 10
num = num // 10
max1 = num % 10

while num > 0:
    num = num // 10
    if max > max1 or max == max1:
        max1 = num % 10
    elif max < max1:
        max = max1

print(f'Наибольшая цифра в веденном числе: {max}')