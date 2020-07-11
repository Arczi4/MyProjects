import numpy as np

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
    if not (pos>=0 and pos<10):
        print("Wybrales złą pozycję! wybierz ponownie")
        pos = int(input('Wybierz pozycje'))
    # player X
    if player_flag:
        board[pos] = 'X'
        player_flag = False
    else:
        board[pos] = 'O'
        player_flag = True
    m_count += 1
    return board


def check_Win(bo, player):
    if player:
        le = 'X'
    else:
        le = 'O'

    return (  # check rows
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


def is_full():
    global m_count
    if m_count <= 9:
        return True
    else:
        print("Brak miejsca na tablicy.\nREMIS! ")
        return False


def Game_1vs1():
    while is_full:
        check_Win_X = check_Win(board,player_flag)
        check_Win_O = check_Win(board, not player_flag)
        if check_Win_X or check_Win_O:
            show_board()
            if player_flag:
                print("Wygrywa X!")

            else:
                print("Wygrywa O!")
            print('Czy chcesz zagrać ponownie?')
            x=int(input('1.Tak\n2.Nie'))
            if x == 1:
                Clear_board()
                main()
            else:
                break

        show_board()
        move(board)

def Game_vsComp():
    pass

def main():
    print("Witaj w grze Tic Tac Toe\n"
          "Wybierz 1. aby zagrać 1 na 1\n"
          "Wybierz 2. aby zagrac z komputerem\n"
          "Wybierz 3. aby wyjść z gry")
    choice = int(input())
    if choice == 1:
        Game_1vs1()
    elif choice == 2:
        Game_vsComp()
    elif choice == 3:
        exit()


main()




