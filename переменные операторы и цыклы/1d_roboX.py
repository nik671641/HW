
size = 180
roboX = 1
a = 21
b = 22
c = 23
d = 24
f = 25
i = 26
j = 34
q = 8
w = 9
e = 10
r = 11
t = 12
y = 13
qw = 14
qe = 46
u = 47
o = 48
p = 49
s = 50
g = 51
h = 52
k = 54
l = 74
z = 94
x = 114
v = 115
m = 116
qr = 117
qa = 72
qs = 92
qd = 112
wq = 132
we = 152
wr = 153
wa = 154
ew = 155
eq = 156
ea = 157
es = 118
ed = 119
ef = 120
eg = 140
er = 160
et = 158
sa = 178
ww = 179
rr = 180


#
while True:
    n = 1
    while n <= size:
        if n == roboX:
            print('🐵 ', end='')
        elif n == a or n == sa or n == rr or n == et or n == eg or n == er or n == ed or n == ef or n == es or n == ea or n == wr or n == wa or n == we or n == ew or n == eq or n == wq or n == qa or n == qs or n == qd or n == b or n == j or n == v or n == m or n == qr or n == z or n == x or n == k or n == l or n == qe or n == c or n == qw or n == d or n == f or n == i or n == q or n == w or n == e or n == r or n == t or n == y or n == u or n == o or n == p or n == s or n == g or n == h:
            print('O  ', end='')
        elif roboX == a or roboX == sa or roboX == rr or roboX == et or roboX == eg or roboX == er or roboX == ed or roboX == ef or roboX == es or roboX == ea or roboX == wr or roboX == wa or roboX == we or roboX == ew or roboX == eq or roboX == wq or roboX == qa or roboX == qs or roboX == qd or roboX == b or roboX == j or roboX == v or roboX == m or roboX == qr or roboX == z or roboX == x or roboX == k or roboX == l or roboX == qe or roboX == c or roboX == qw or roboX == d or roboX == f or roboX == i or roboX == q or roboX == w or roboX == e or roboX == r or roboX == t or roboX == y or roboX == u or roboX == o or roboX == p or roboX == s or roboX == g or roboX == h:
            roboX = 2
        elif n == ww:
            print('⚑  ', end='')
        elif roboX == ww:
            print('\n              YOU WIN!!!')
            break
        elif n <= size:
            print('+  ', end='')
        if n % 20 == 0:
            print()

        n += 1
    print('')

    direction = input('write (w/s/a/d/ "/") >>')
    if direction == 'a':
        roboX -= 1
    if direction == 'd':
        roboX += 1
    if direction == 's':
        roboX += 20
    if direction == 'w':
        roboX -= 20
    if direction == "/":
        roboX = 1
