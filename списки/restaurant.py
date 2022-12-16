food_name = ['Pizza', 'Soup', 'Salad']
food_price = [100, 50, 25]

status = ['free', 'free', 'free']
client = ['', '', '']
dishes = ['', '', '']
bill = [0.0, 0.0, 0.0]
tip = [0.0, 0.0, 0.0]

# client[0] = 'Marry'
# status[0] = 'not free'

# client[1] = 'Kate'
# status[1] = 'not free'

# client[2] = 'John'
# status[2] = 'not free'

qwe = input("What's your name? :")
qwq = int(input('Choose a table: '))
if qwq == 1:
    client.append(0)
if qwq == 2:
    client.append(1)
if qwq == 3:
    client.append(2)


order_dish = 'Soup'
client_name = qwe
table_idx = -1

for ti in range(len(client)):
    if client[ti] == client_name:
        table_idx = ti
        break
food_idx = -1
for fi in range(len(food_name)):
    if food_name[fi] == order_dish:
        food_idx = fi
        break
dishes[table_idx] = order_dish
bill[table_idx] = food_price[food_idx]
tip[table_idx] = bill[table_idx] * 0.1

for ti in range(len(status)):
    print(f'{ti} : {status[ti]}')
    if status[ti] != 'free':
        print(f'\t {client[ti]} : {dishes[ti]} -> {bill[ti]}')
        print(f'\t % {tip[ti]}')
