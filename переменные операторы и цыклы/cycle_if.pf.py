from time import sleep


m_title_1 = 'Аватар 2 Анонс'
m_title_2 = 'Тор: Любовь и гром'
m_title_3 = 'Морбиус'

m_1_ticet_a_cost = 25
m_1_ticet_b_cost = 50
m_1_ticet_c_cost = 100


print(f'''
1. {m_title_1}
     Дата премьеры состоится 16 декабря 2022 г. в США
     Жанр: Научная фантастика/Приключения
     В кинотеатрах 28 декабря в:
        a. 14:00
        b. 17:20
        c. 22:00 VIP места
2. {m_title_2}
     Дата премьеры состоялась 1 апреля 2022 г. в США
     Жанр: Боевик/Фэнтези
     В кинотеатрах 21 ноября в:
        a. 13:00
        b. 18:00
        c. 21:00 VIP места
3. {m_title_3}
     Дата премьеры состоялась 6 июля 2022 г. в Австралии
     Жанр: Боевик/Фэнтези
     В кинотеатрах 18 ноября в:
        a. 15:00
        b. 20:00
        c. 23:00 VIP места   
''')

movie_number = int(input('Выбери фильм: '))

if movie_number == 1:

    print(f'Ты выбрал Фильм"{m_title_1}"')
    time = input('\nВыбери время: ')
    cost = 0

    if time == 'a':
        print(f'Время: 14:00, стоимоть билета {m_1_ticet_a_cost}$')
        cost = 25

    if time == 'b':
        print(f'Время: 17:00, стоимоть билета {m_1_ticet_b_cost}$')
        cost = 50

    if time == 'c':
        print(f'Время: 22:00, стоимоть билета {m_1_ticet_c_cost}$ VIP места ')
        cost = 100

    amound = int(input('\nСколько билетов: '))
    total = amound * cost

    print(f'{amound} x {cost} = {total}$')

if movie_number == 2:

    print(f'Ты выбрал Фильм"{m_title_2}"')
    time = input('\nВыбери время: ')
    cost = 0

    if time == 'a':
        print(f'Время: 13:00, стоимоть билета {m_1_ticet_a_cost}$')
        cost = 25

    if time == 'b':
        print(f'Время: 18:00, стоимоть билета {m_1_ticet_b_cost}$')
        cost = 50

    if time == 'c':
        print(f'Время: 21:00, стоимоть билета {m_1_ticet_c_cost}$ VIP места ')
        cost = 100

    amound = int(input('\nСколько билетов: '))
    total = amound * cost

    print(f'{amound} x {cost} = {total}$')

if movie_number == 3:

    print(f'Ты выбрал Фильм"{m_title_3}"')
    time = input('\nВыбери время: ')
    cost = 0

    if time == 'a':
        print(f'Время: 15:00, стоимоть билета {m_1_ticet_a_cost}$')
        cost = 25

    if time == 'b':
        print(f'Время: 20:00, стоимоть билета {m_1_ticet_b_cost}$')
        cost = 50

    if time == 'c':
        print(f'Время: 23:00, стоимоть билета {m_1_ticet_c_cost}$ VIP места ')
        cost = 100

    amound = int(input('\nСколько билетов: '))
    total = amound * cost

    print(f'{amound} x {cost} = {total}$')

sleep(2)
print('\nСпасибо за покупку\nИ прияного просмотра))')
