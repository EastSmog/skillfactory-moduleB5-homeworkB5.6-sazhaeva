play_field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def field(f):
    num_string = [str(i) for i in range(3)]
    num_columns = '  0 1 2'

    full_field = zip(num_string, f)
    print(num_columns)
    for j, i in full_field:
        print(f"{j} {' '.join(i)}")
    print('')
    return 'Победа!'


def correct_input(f, user):
    while True:
        cell = input(f'Сделайте свой ход, Игрок-{user}: ').split()
        if len(cell) != 2:
            print('Введите две координаты')
            print('')
            continue
        if not (cell[0].isdigit() and cell[1].isdigit()):
            print('Координаты должны быть числами')
            print('')
            continue
        x, y = int(cell[0]), int(cell[1])
        if not (0 <= x < 3) or not (0 <= y < 3):
            print('Координаты за пределами диапазона поля')
            print('')
            continue
        if f[x][y] == 'X' or f[x][y] == 'O':
            print('Координаты уже были испльзованы ранее')
            print('')
            continue
        break
    return x, y


def find_winner(f, user):
    f_list = []
    for obj in f:
        f_list += obj
    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indexes = set([i for i, x in enumerate(f_list) if x == user])
    for p in positions:
        if len(indexes.intersection(set(p))) == 3:
            return True
    return False


def rules(f):
    print('Добро пожаловать в игру крестики-нолики!')
    print('Правила игры')
    print(f'В игре участвуют два игрока. Игроки по очереди ставят на свободные клетки поля 3×3 знаки'
          '\n'
          '(один всегда крестики, другой всегда нолики). Первый игрок,'
          '\n'
          'выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.'
          '\n'
          ' Первый ход делает игрок, ставящий крестики.')
    print('Механика игры')
    print('Чтобы сделать ход, игрок указывает координаты клетки поля, на которую хочет поставить знак.'
          '\n'
          'Координаты представляют собой два числа в диапазоне от 0 до 2 каждое и вводятся через пробел')
    play_start = input('Если хотите начать игру, введите S: ')
    if play_start == 'S':
        start(f)
    if play_start != 'S':
        print('До встречи!')



def last_field(f):
    return field(f)


def start(f):
    count = 0
    print('')
    print('Поехали!')
    while True:
        print('')
        field(f)
        if count % 2 == 0:
            user = 'X'
        else:
            user = 'O'
        if count < 9:
            x, y = correct_input(f, user)
            f[x][y] = user

        elif count == 9:
            print('Ничья')
            break
        if find_winner(f, user):
            print('\n')
            print(f"Поздравляем, Игрок-{user},")
            print('\n')
            print(last_field(f))
            break
        count += 1


rules(play_field)