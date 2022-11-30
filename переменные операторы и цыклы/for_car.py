roadlan = 10
carY = 1
line = 2
qwq = '---------'

while True:
    print(qwq)
    for y in range(roadlan, 0, -1):
        carL = ' '
        carR = ' '
        if y == carY:
            if line == 1:
                carL = '#'
            if line == 2:
                carR = '#'
        print(f'| {carL} : {carR} |')

    print(qwq)

    move = input('(w,s,a,d) >>')
    if move == 'w':
        carY += 1
    if move == 's':
        carY -= 1
    if move == 'a':
        if line == 2:
            line = 1
    if move == 'd':
        if line == 1:
            line = 2
    if carY > 10:
        carY = 1
    if carY < 1:
        carY = 1
