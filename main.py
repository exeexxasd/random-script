import random

def ran_f():
    rand_val = int(input('Введите число которое хотите найти: '))
    max_val = int(input('Введите максимальное кол-во попыток: '))
    first_val = int(input('Введите число с которого начать случайный выбор:'))
    second_val = int(input('Введите число на котором закончить случайный выбор:'))
    x = ()
    i = (1)
    while x != rand_val and i < max_val:
        x = random.randrange(first_val, second_val)
        #print(x, i)
        i += 1
        if  i == max_val:
            print(f'Слишком много попыток (>{max_val}).')
    if x == rand_val: print('На это потребовалось', i - 1, 'попыток.')

def random_int():
    first = int(input('Введите число с которого начать случайный выбор:'))
    second = int(input('Введите число на котором закончить случайный выбор:'))
    while second < first:
        print('Второе число не может быть меньше первого.')
        first = int(input('Введите число с которого начать случайный выбор:'))
        second = int(input('Введите число на котором закончить случайный выбор:'))

    print('Случайное число между', first, 'и', second, ':',random.randrange(first, second))


choise = int(input('Выберите функцию которую хотите использовать (1 | 2):'))
if choise == 1: ran_f()
if choise == 2: random_int()

input("Press enter to exit;")

