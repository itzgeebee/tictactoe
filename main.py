from time import sleep



played_keys = []

INSTRUCTIONS = "Here are the rules to the game:" \
               "RULES FOR TIC-TAC-TOE " \
               "1. The game is played on a grid that's 3 squares by 3 squares.\n" \
               "2. Player 1 is X, player 2  is O. Players take turns putting their marks in empty squares.\n" \
               "3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n" \
               "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in\n " \
               "a tie. \n" \
               "5. For this game you would be using positions(11-33) to place your X's or O's e.g\n" \
               "11 stands for row 1 column 1 which is the topmost left most position and 33 stands for the last position\n" \
               "which is the bottommost rightmost position and 22 stands for the second row of the second column\n" \
               "which is dead centre of the board.\n" \
               "[11, 12, 13]\n" \
               "[21, 22, 23]\n" \
               "[31, 32, 33]\n" \
               "Enjoy\n"


def update_board(player, played, board):
    pos_num_1 = int(played[0])
    pos_num_2 = int(played[1])
    if player == "player_1":
        board[pos_num_1 - 1][pos_num_2 - 1] = "X"
    else:
        board[pos_num_1 - 1][pos_num_2 - 1] = "O"

    return board


def first_player(board):
    player_1 = input("player 1's turn: ")
    player = "player_1"
    result = check_valid_keys(player_1)
    if result == "good":
        update_board(player, player_1, board)
        for i in range(3):
            print(board[i])

    else:
        print("can't play that")
        first_player(board)


def second_player(board):
    player_2 = input("player 2's turn: ")
    player = "player_2"
    result = check_valid_keys(player_2)
    if result == "good":
        update_board(player, player_2, board)
        for i in range(3):
            print(board[i])

    else:
        print("can't play that")
        second_player(board)


def check_valid_keys(key):
    valid_keys = [11, 12, 13, 21, 22, 23, 31, 32, 33]
    try:
        if int(key) in valid_keys and key not in played_keys:
            played_keys.append(key)
            return "good"
        else:
            return "bad"
    except ValueError:
        return "bad"


def draw(box):
    a = box[0].count("-")
    b = box[1].count("-")
    c = box[2].count("-")

    # print("a", a)
    # print("b", b)
    # print("c", c)

    return (a + b + c) == 0


def p1_win_conditions(board):
    pos_1 = board[0][0]
    pos_2 = board[0][1]
    pos_3 = board[0][2]
    pos_4 = board[1][0]
    pos_5 = board[1][1]
    pos_6 = board[1][2]
    pos_7 = board[2][0]
    pos_8 = board[2][1]
    pos_9 = board[2][2]

    if pos_1 == "X" and pos_2 == "X" and pos_3 == "X":
        return True
    if pos_4 == "X" and pos_5 == "X" and pos_6 == "X":
        return True
    if pos_7 == "X" and pos_8 == "X" and pos_9 == "X":
        return True
    if pos_1 == "X" and pos_4 == "X" and pos_7 == "X":
        return True
    if pos_2 == "X" and pos_5 == "X" and pos_8 == "X":
        return True
    if pos_3 == "X" and pos_6 == "X" and pos_9 == "X":
        return True
    if pos_1 == "X" and pos_5 == "X" and pos_9 == "X":
        return True
    if pos_3 == "X" and pos_5 == "X" and pos_7 == "X":
        return True


def p2_win_conditions(board):
    pos_1 = board[0][0]
    pos_2 = board[0][1]
    pos_3 = board[0][2]
    pos_4 = board[1][0]
    pos_5 = board[1][1]
    pos_6 = board[1][2]
    pos_7 = board[2][0]
    pos_8 = board[2][1]
    pos_9 = board[2][2]

    if pos_1 == "O" and pos_2 == "O" and pos_3 == "O":
        return True
    if pos_4 == "O" and pos_5 == "O" and pos_6 == "O":
        return True
    if pos_7 == "O" and pos_8 == "O" and pos_9 == "O":
        return True
    if pos_1 == "O" and pos_4 == "O" and pos_7 == "O":
        return True
    if pos_2 == "O" and pos_5 == "O" and pos_8 == "O":
        return True
    if pos_3 == "O" and pos_6 == "O" and pos_9 == "O":
        return True
    if pos_1 == "O" and pos_5 == "O" and pos_9 == "O":
        return True
    if pos_3 == "O" and pos_5 == "O" and pos_7 == "O":
        return True


def keep_scores():
    player_1_score = 0
    player_2_score = 0
    return f""

def play_game():
    print(INSTRUCTIONS)
    consent = input("Play a game of X and O? Y/N ").lower()
    if consent == "y":
        main_box = [["-", "-", "-"]
            , ["-", "-", "-"],
                    ["-", "-", "-"]]
        for i in main_box:
            print(i)
        game_on = True
        while game_on:

            first_player(main_box)
            if p1_win_conditions(main_box):
                print("player 1 wins")
                game_on = False
                sleep(2)
                play_game()

            else:
                second_player(main_box)
                if p2_win_conditions(main_box):
                    print("player 2 wins")
                    game_on = False
                    sleep(2)
                    play_game()

            if draw(main_box):
                print("it's a draw")
                game_on = False
                sleep(2)
                play_game()
    else:
        print("hope you play next time")
        return


play_game()
