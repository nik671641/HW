import random

N = random.randint(1, 1_000_000)

for tries in range(1, ):
    n = random.randint(0, 1_000_000)
    if n == N:
        print('You Win!!!')
        break
    elif n < N:
        print('Число больше')
    else:
        print('Число меньше')
