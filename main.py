import random
from time import sleep

played_keys = [] #keeps track of all the entered numbers
player_scores =[0,0] # keeps track of player scores


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
               "Position guide below:\n" \
               "[11, 12, 13]\n" \
               "[21, 22, 23]\n" \
               "[31, 32, 33]\n" \
               "Enjoy\n"


def update_board(player, played, board):
    """ takes in 3 arguments, the player, the number played and the tictactoe array and updates
    the position with either 'X' or 'O'
    returns the updated board"""
    pos_num_1 = int(played[0])
    pos_num_2 = int(played[1])
    if player == "player_1":
        board[pos_num_1 - 1][pos_num_2 - 1] = "X"
    else:
        board[pos_num_1 - 1][pos_num_2 - 1] = "O"

    return board

def display_board(board):
    """displays the board in presentable print format"""
    print(f"---------------------------")
    print(f"   {board[0][0]}    |    {board[0][1]}    |   {board[0][2]}   ")
    print(f"---------------------------")
    print(f"   {board[1][0]}    |    {board[1][1]}    |   {board[1][2]}   ")
    print(f"---------------------------")
    print(f"   {board[2][0]}    |    {board[2][1]}    |   {board[2][2]}   ")
    print(f"---------------------------")


def first_player(board):
    """ takes in a single argument(the game array) and controls player 1 behaviour"""
    player_1 = input("player 1's turn: ")
    player = "player_1"
    result = check_valid_keys(player_1)
    if result == "good":
        update_board(player, player_1, board)
        display_board(board)

    else:
        print("can't play that")
        first_player(board)


def second_player(board):
    """ takes in a single argument(the game array) and controls player 2 behaviour"""
    player_2 = input("player 2's turn: ")
    player = "player_2"
    result = check_valid_keys(player_2)
    if result == "good":
        update_board(player, player_2, board)
        display_board(board)

    else:
        print("can't play that")
        second_player(board)

def check_valid_keys(key):
    """ takes in one argument; user input and validates it. returns either 'good' or 'bad' """
    valid_keys = [11, 12, 13, 21, 22, 23, 31, 32, 33]

    try:

        print(played_keys)
        if int(key) in valid_keys and key not in played_keys:
            played_keys.append(key)
            return "good"
        else:
            return "bad"
    except ValueError:
        return "bad"


def draw(box):
    """takes in one argument (game array) and checks the condition for a tie. returns True or False"""
    a = box[0].count(" ")
    b = box[1].count(" ")
    c = box[2].count(" ")

    return (a + b + c) == 0


def p1_win_conditions(board):
    """takes in one argument (game array) and checks if condition for a win are met. returns True or False"""
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
    """takes in one argument (game array) and checks if condition for a win are met. returns True or False"""
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


def display_scores(scores):
    """formats player scores in print format"""
    print(f"player one  {scores[0]}  |  {scores[1]} player two")


def play_game():
    """ contains the logical flow of the game. takes no argument"""
    consent = input("Play a game of X and O? Y/N ").lower()
    if consent == "y":
        print(INSTRUCTIONS)
        main_box = [[" ", " ", " "]
            , [" ", " ", " "],
                    [" ", " ", " "]]
        played_keys.clear()

        display_board(main_box)
        game_on = True
        while game_on:
            display_scores(player_scores)

            first_player(main_box)
            if draw(main_box):
                print("it's a tie 🤜🤛")
                display_scores(player_scores)
                game_on = False
                sleep(4)
                play_game()

            elif p1_win_conditions(main_box):
                print("player 1 wins 🎉🎉👏👏")
                player_scores[0] += 1
                display_scores(player_scores)
                game_on = False
                sleep(4)
                play_game()


            else:
                second_player(main_box)
                if p2_win_conditions(main_box):
                    print("player 2 wins 🎉🎉👏👏")
                    player_scores[1] += 1
                    display_scores(player_scores)
                    game_on = False
                    sleep(4)
                    play_game()


    else:
        print("come back next time")
        return


play_game()
