import random
import os.path
import json

random.seed()


def draw_board(board):
    print("------------")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("------------")


def welcome(board):
    print("Welcome to Noughts and Crosses!\n")
    draw_board(board)  # After it prints the above welcome message it calls the draw_board method


def initialise_board(board):
    for i in range(9):
        board.append(" ")
    return board  # creates the board spaces generate din draw board


def get_player_move(board):
    print("Your move (1-9): ", end="")
    move = int(input().strip())  # In order to remove any blank spaces, we take the user's input on the range (1-9)
    row, col = (move-1)//3, (move-1) % 3  # The index of each row and col is reached.
    while board[row * 3 + col] != ' ':  # Determines if the available board space is available or not.
        print("The cell is not empty. Try Again!")  # This output is shown if it's occupied.
        print("Your move (1-9): ", end="")  # And continues asking
        move = int(input().strip())
        row, col = (move - 1) // 3, (move - 1) % 3
    board[row * 3 + col] = 'X'  # Determines the cell's row and col indices after applying the 'X' definition.
    return row, col


def choose_computer_move(board):
    free_cells = [i for i in range(9) if board[i] == " "]  # Creates a "free_cells" with empty spaces
    move = random.choice(free_cells)  # Chooses the random cell in the "free_cells" list
    row, col = move//3, move % 3
    board[row * 3 + col] = 'O'  # Determines the cell's row and col indices after applying the 'O' defination.
    return row, col


def check_for_win(board, mark):
    #Tuples develops for the sake of winning.
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for row, col1, col2 in win_conditions:
        if board[row] == board[col1] == board[col2] == mark:
            return True
    # It will return false if no tuples are true.
    return False


def check_for_draw(board):
    # It will return true if the cells are fields.
    return not " " in board


def play_game(board):
    # calls the board and welcome message
    initialise_board(board)
    welcome(board)
    while True:
        row, col = get_player_move(board)
        draw_board(board)
        #determines whether "X" wins and returns 1 if it does.
        if check_for_win(board, 'X'):
            return 1
        # When cells are not empty, 0 is returned.
        elif check_for_draw(board):
            return 0
        row, col = choose_computer_move(board)
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        elif check_for_draw(board):
            return 0


def menu():
    print("1 - Let's start the game")
    print("2 - Scores's save in  'leaderboard.txt'")
    print("3 - Load and display the scores from the 'leaderboard.txt'")
    print("q - End the program")
    choice = input("Enter your choice: ")
    return choice


def load_scores():
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            leaders = json.load(file)
    return leaders


def save_score(score):
    player_name = input("Enter your name: ")
    leaders = load_scores()
    leaders[player_name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaders, file)
        
    print("\t--------------------------------\n")
def display_scores(leaders):  
    print("leaderboard:")
    for name, score in leaders.items():
        print("{}: {}".format(name,score))
   
    print("\t--------------------------------\n")



def update_scores(leaders, result):
    name = input("what is your name: ")
    if name in leaders:
        leaders[name] += result
    else:
        leaders[name] = result
    with open("leaderboard.txt", "w") as file:
        json.dump(leaders, file)


def main():
    leaders = load_scores()
    board = []
    while True:
        choice = menu()
        if choice == 'q':
            break
        if choice == '1':
            result = play_game(board)
            if result == 1:
                print("You won!")
            elif result == 0:
                print("Draw.")
            elif result == -1:
                print("You lost.")
        elif choice == '2':
            update_scores(leaders, result)
        elif choice == '3':
            display_scores(leaders)


if __name__ == '__main__':
    main()
