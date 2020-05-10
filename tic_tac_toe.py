import random
 
#Welcome Message
print('''    Welcome to the Tic-Tac-Toe game!
This game is played between two players.
             GOOD LUCK!\n''')

#Asks the players their name
def replay():
    global player1, player2, selection
    player1 = input("Enter name of first player: ")
    player2 = input("Enter name of second player: ")
    #Ask player 1 to be either X or O
    selection = input(f"{player1}: Do you want to be X or O? Choose: ")

#The main tic-tac-toe board where the action takes place
def display_board():
    print("\n"*5)
    print('''
     |     |          |          |     | 
  1  |  2  |  3       |       {}  |  {}  |  {}
     |     |          |          |     |
-----------------     |     -----------------
     |     |          |          |     |
  4  |  5  |  6       |       {}  |  {}  |  {}
     |     |          |          |     |
-----------------     |     -----------------
     |     |          |          |     |
  7  |  8  |  9       |       {}  |  {}  |  {}
     |     |          |          |     |'''.format(board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8],board[9]))

#Brain of the code
def board_list():
    global board, to_go_first
    board = [" "," "," "," "," "," "," "," "," "," "]
    moves = 0

    #Calls the display_board() function
    display_board()

    #To select which player goes first
    to_go_first = random.choice(["X", "O"])
    if selection.upper() == to_go_first:
        print(f"{player1} will go first.")
        first, second = player1, player2
    else:
        print(f"{player2} will go first.")
        first, second = player2, player1

    if to_go_first == "X":
        placeholder = ("X","O")
    else:
        placeholder = ("O","X")
    
    #Fills up the board list after each move
    while moves < 10:
        number = int(input("Choose your next position (1-9): "))
        #for player 1
        if moves % 2 == 0:
            board[number] = placeholder[0]   
            display_board()
            check_if_win()
            if end != False:
                print(f"{first} has won the game!!!")
                break
        #for player 2
        else:
            board[number] = placeholder[1]
            display_board()
            check_if_win()
            if end != False:
                print(f"{second} has won the game!!!")
                break
                
        moves += 1
        if moves != 9:
            continue
        else:
            print("It's a Draw!!")
            break

#Determine if player won or not.
def check_if_win():
    global end
    end = False
    if (board[1] == board[2] == board[3] != " " or #top horizontal
        board[1] == board[4] == board[7] != " " or #left vertical
        board[1] == board[5] == board[9] != " " or #main diagonal
        board[2] == board[5] == board[8] != " " or #middle vertical
        board[3] == board[6] == board[9] != " " or #right vertical
        board[3] == board[5] == board[7] != " " or #auxiliary diagonal
        board[4] == board[5] == board[6] != " " or #middle horizontal
        board[7] == board[8] == board[9] != " "):  #bottom horizontal
        end = True

#The code is controlled from here
def main():
    play = input("Are you ready to play? Enter Yes or No: ")
    print("\n")
    while play.lower() == "yes":
        replay()
        board_list()
        play = input("Do you want to play again? Enter Yes or No: ")
    
main()
