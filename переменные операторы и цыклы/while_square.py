size = 120  # int(input('size: '))<--------\
cize = 60  # int(input('cize: '))<---------|-------можно и так, но для сабильность кода я сделал так
dize = 120  # int(input('dize: '))<--------/                                            /
#     /\                                                                               /
#      \------------------------------------------------------------------------------/

n = 1
z = 1
h = 1

while n <= size:
    print('+ ', end='')
    if n == 30 or n == 60 or n == 90 or n == 120 or n == 150 or n == 180:
        print()
    n += 1

while z <= cize:
    print('+ ', end='')
    if z % 6 == 0:
        print('                                    + + + + + +')
    z += 1

while h <= dize:
    print('+ ', end='')
    if h == 30 or h == 60 or h == 90 or h == 120 or h == 150 or h == 180:
        print()
    h += 1

