import numpy as np

# create board
board = ['0', '1', '2',
         '3', '4', '5',
         '6', '7', '8']

player_flag = True
game = True


# board display
def show_board():
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print('-' * 13)
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print('-' * 13)
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')
    print('-' * 13)


# player move
# chceck player X(TRUE def) or O(FALSE)
def move():
    global player_flag
    pos = int(input('take a position 0-8'))
    # player X
    if player_flag:
        board[pos] = 'X'
        player_flag = False
    else:
        board[pos] = 'O'
        player_flag = True


def check_Win(bo, player):
    if player:
        le = 'X'
    else:
        le = 'O'

    return not ( # check rows
            (bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or

            # check columns
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[3] == le and bo[5] == le and bo[8] == le) or

            # check diagonals
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))



while game:

    show_board()
    move()
    game = check_Win(board, player_flag)
    if not game:
        if player_flag:
            print("Wygrywa gracz X")
        else:
            print("Wygrywa gracz O")
