import base64

print('Введите операцию: ')
operation = int(input(' 1. Умножение\n 2. Деление\n 3. Сложение\n 4. Вычитание\n 5. Остаток от деления\n 6. Целочисленное деление\n 7. Длина\n'
                      ' 8. Валюты\n 9. Веса\n 10. Доходность вклада\n '))
if operation == 1:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    print(num_1 * num_2)
if operation == 2:
    num_3 = int(input('Введите первое число: '))
    num_4 = int(input('Введите второе число: '))
    print(num_3 / num_4)
if operation == 3:
    num_5 = int(input('Введите первое число: '))
    num_6 = int(input('Введите второе число: '))
    print(num_5 + num_6)
if operation == 4:
    num_7 = int(input('Введите первое число: '))
    num_8 = int(input('Введите второе число: '))
    print(num_7 - num_8)
if operation == 5:
    num_9 = int(input('Введите первое число: '))
    num_10 = int(input('Введите второе число: '))
    print(num_9 % num_10)
if operation == 6:
    num_11 = int(input('Введите первое число: '))
    num_12 = int(input('Введите второе число: '))
    print(num_11 // num_12)
if operation == 7:
    dlina = int(input(' 1. Метры в сантиметры\n 2. Сантиметры в метры\n '))
    if dlina == 1:
        mter = int(input('Введите количество метров: '))
        print(mter * 1000, 'сантиметров')
    if dlina == 2:
        sm = int(input('Введите количество сантиметров: '))
        print(sm / 1000, 'метров')
if operation == 8:
    valuta = int(input(' 1. Рубли в доллары\n 2. Доллары в рубли\n 3. Рубли в евро\n 4. Евро в рубли\n '))
    if valuta == 1:
        rub = int(input('Введите количество рублей: '))
        print(rub / 60, 'долларов')
    if valuta == 2:
        dol = int(input('Введите количество долларов: '))
        print(dol * 60, 'рублей')
    if valuta == 3:
        rub_2 = int(input('Введите количество рублей: '))
        print(rub_2 / 70, 'евро')
    if valuta == 4:
        ev = int(input('Введите количество евро: '))
        print(ev * 70, 'евро')
if operation == 9:
    ves = int(input(' 1. Киллограммы в граммы\n 2. Граммы в килограммы\n '))
    if ves == 1:
        ves_1 = int(input('Введите количество килограммов: '))
        print(ves_1 * 1000, 'граммов')
    if ves == 2:
        ves_2 = int(input('Введите количество граммов: '))
        print(ves_2 / 1000, 'килограммов')
if operation == 10:
    vklad = int(input(' Какую сумму вносите: '))
    potent = int(input(' Какой процент у вклада: '))
    year = int(input(' На сколько лет делаете вклад: '))
    print((vklad / 100) * potent * year, ' рублей доходность вклада за период')




