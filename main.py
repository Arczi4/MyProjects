# create board
board = ['0', '1', '2',
         '3', '4', '5',
         '6', '7', '8']
player_flag = True


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


while 1:
    show_board()
    move()