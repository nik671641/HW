import os

SIZE = [8, 8]
EMPTY = 0
WKING = 1
WQUEEN = 2
WBISHOP = 3
WKNIGHT = 4
WPAWN = 6
WROOK = 5

BKING = 11
BQUEEN = 12
BBISHOP = 13
BKNIGHT = 14
BPAWN = 16
BROOK = 15

board = [
    [5, 4, 3, 1, 2, 3, 4, 5],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],


]
black = ' ♚♛♝♞♜♟'

pieces       = [' ', 'KI', 'QU', 'BI', 'KN', 'RO', 'PA']
pieces_codes = [' ', 'ki', 'qu', 'bi', 'kn', 'ro', 'pa']
alphabet = 'abcdefgh'
game_over = False
while not game_over:
    print(' ', end='')
    os.system('cls')
    for e in alphabet:
        print(f'{e:^5}', end='')
    print()
    for ri in range(SIZE[0]):
        print(' -' + '-----' * SIZE[1])
        rc = SIZE[0] - ri
        print(rc, end='')
        for ci in range(SIZE[1]):
            piece = pieces[board[ri][ci]]
            print(f'|{piece:^4}', end='')
        print('|')
    print(' -' + '-----' * SIZE[1])

    move = input('your move >>')
    what, from_, to_ = move[0:2], move[2:4], move[4:6]
    print(what, from_, to_)
    if what not in pieces_codes:
        print('Wrong piece code!!!')
    else:
        piece_code = pieces_codes.index(what)
        ri_from = SIZE[0] - int(from_[1])
        ci_from = alphabet.index(from_[0])

        ri_to = SIZE[0] - int(to_[1])
        ci_to = alphabet.index(to_[0])
        print(piece_code, ri_from, ci_from)
        print(piece_code, ri_to, ci_to)

        if board[ri_from][ci_from] == piece_code:
            board[ri_from][ci_from] = EMPTY
            board[ri_to][ci_to] = piece_code
        else:
            print('the piece you try to move is not there')
    input()
# pad7d6