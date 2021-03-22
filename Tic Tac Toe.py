board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    i = 1
    display_board()
    while "-" in board:
        if i % 2 != 0:
            turn = 'X'
            user_in = input(f"You are {turn}. Select position from 1 - 9: ")
            position = int(user_in) - 1
            board[position] = turn
            display_board()
            i += 1
            if (
                    (board[0] == turn and board[3] == turn and board[6] == turn) or
                    (board[1] == turn and board[4] == turn and board[7] == turn) or
                    (board[2] == turn and board[5] == turn and board[8] == turn) or
                    (board[0] == turn and board[1] == turn and board[2] == turn) or
                    (board[3] == turn and board[4] == turn and board[5] == turn) or
                    (board[6] == turn and board[7] == turn and board[8] == turn) or
                    (board[0] == turn and board[4] == turn and board[8] == turn) or
                    (board[2] == turn and board[4] == turn and board[6] == turn)
            ):
                print(f"{turn} WINS!")
                break
            else:
                pass
        else:
            turn = 'O'
            user_in = input(f"You are {turn}. Select position from 1 - 9: ")
            position = int(user_in) - 1
            board[position] = turn
            display_board()
            i += 1
            if (
                    (board[0] == turn and board[3] == turn and board[6] == turn) or
                    (board[1] == turn and board[4] == turn and board[7] == turn) or
                    (board[2] == turn and board[5] == turn and board[8] == turn) or
                    (board[0] == turn and board[1] == turn and board[2] == turn) or
                    (board[3] == turn and board[4] == turn and board[5] == turn) or
                    (board[6] == turn and board[7] == turn and board[8] == turn) or
                    (board[0] == turn and board[4] == turn and board[8] == turn) or
                    (board[2] == turn and board[4] == turn and board[6] == turn)
            ):
                print(f"{turn} WINS!")
                break
            else:
                pass


play_game()