import random as rand

# create board
board = ['0', '1', '2',
         '3', '4', '5',
         '6', '7', '8']

player_flag = True
game = True

# movement count
m_count = 0


def Clear_board():
    global board
    board = ['0', '1', '2',
             '3', '4', '5',
             '6', '7', '8']


# board display
def show_board():
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print('-' * 13)
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print('-' * 13)
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')
    print('-' * 13)


# player move
# chceck player X(TRUE def)  O(FALSE)
def move(board):
    global player_flag
    global m_count
    pos = int(input('take a position 0-8'))
    if not (pos >= 0 and pos < 10):
        print("Wybrales złą pozycję! wybierz ponownie")
        pos = int(input('Wybierz pozycje'))
    # player X
    if player_flag:
        board[pos] = 'X'
        player_flag = False
        m_count += 1
    else:
        board[pos] = 'O'
        player_flag = True
        m_count += 1
    return board


def check_Win(bo, le):
    return (  # check rows
            (bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or

            # check columns
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or

            # check diagonals
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))


def is_full():
    global m_count
    if m_count == 8:
        return True
    else:
        print("Brak miejsca na tablicy.\nREMIS! ")
        return False


def Game_1vs1():
    while is_full:
        check_Win_X = check_Win(board, 'X')
        check_Win_O = check_Win(board, 'O')
        if check_Win_X or check_Win_O:
            if check_Win_X:
                show_board()
                print("Wygrywa X!")
            else:
                show_board()
                print("Wygrywa O!")

            print('Czy chcesz zagrać ponownie?')
            x = int(input('1.Tak\n2.Nie'))
            if x == 1:
                Clear_board()
                main()
            else:
                break

        show_board()
        move(board)


def Comp_move():
    global m_count

    points = [i for i, letter in enumerate(board) if letter not in ("X", "O")]
    print(points)
    for x in points:
        bo_copy = board[:]
        bo_copy[x] = 'X'
        if check_Win(bo_copy, 'X'):
            board[x] = 'O'
            print("Computer insert \'O\' in place", x)
            break
        else:
            r = rand.choice(points)
            board[r] = 'O'
            print("Computer insert \'O\' in place", r)
            break
    m_count += 1

def Game_vsComp():
    global player_flag
    global m_count

    while is_full:
        print(m_count)
        check_Win_X = check_Win(board, 'X')
        check_Win_O = check_Win(board, 'O')
        if check_Win_X or check_Win_O:
            if check_Win_X:
                show_board()
                print("Wygrywa X!")
            else:
                show_board()
                print("Wygrywa O!")

            print('Czy chcesz zagrać ponownie?')
            x = int(input('1.Tak\n2.Nie'))
            if x == 1:
                Clear_board()
                main()
            else:
                break
        show_board()

        # If play_flag==True -> 'X' player move
        if player_flag:
            move(board)
            player_flag = False

        else:  # If play_flag==False -> 'O' comp move
            Comp_move()
            player_flag = True


def main():
    choice = int(input("Witaj w grze Tic Tac Toe\n"
                       "Wybierz 1. aby zagrać 1 na 1\n"
                       "Wybierz 2. aby zagrac z komputerem\n"
                       "Wybierz 3. aby wyjść z gry"))
    if choice == 1:
        Game_1vs1()
    elif choice == 2:
        Game_vsComp()
    elif choice == 3:
        exit()


main()
