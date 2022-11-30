DUR_UP = -1
DIR_STOPED = 0
DIR_DOWN = 1

building_roof = True
building_floors = 9
building_parking = True

qw = False
we = True
lift_floor = 3
lift_open = True
lift_dir = DIR_STOPED

human_floor = 3
human_in_lift = True

if building_roof:
    print('---|-----|----')
    print(' R |     |    ')
elif building_roof == qw or building_roof == building_floors:
    d = '|---|'
    print(f'---|{d}|----')

for floor in range(9, 0, -1):
    if floor == lift_floor - 1 or floor == lift_floor:
        b = '|---|'
        print(f'---|{b}|----')
    else:
        b = '     '
        print(f'---|{b}|----')
    if floor == human_floor and not human_in_lift:
        h = ' H   '
    else:
        h = '     '

    if floor == lift_floor + 1:
        if lift_open:
            l = ' < > '
        else:
            if lift_dir == DUR_UP:
                l = '  ^  '
            elif lift_dir == DIR_DOWN:
                l = '  v  '
            else:
                l = '     '

    else:
        l = '     '
    if floor == lift_floor:
        l = '|   |'
    elif human_floor == we and lift_floor:
        l = '| H |'
    print(f'{floor:^3}|{l}|{h}')

if building_parking:
    print('---|     |----')
    print(' P |     |    ')
    print('---|-----|----')
elif building_parking == qw:
    print('---|-----|----')
