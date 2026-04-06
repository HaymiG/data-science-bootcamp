board = [" " for _ in range(9)]
current_player = "X"
winner = None
game_running = True                     
# printing the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

print_board(board)
#take player input
def player_input(board):
    inp = int(input("Select a spot 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == " ":
         board[inp-1] = current_player
    elif inp < 1 or inp > 9:
        print("Invalid input. Please select a spot between 1 and 9.")
    else:
        print("Oops player is already at that spot.")
#check win or tie again
while game_running:
    print_board(board)
    player_input(board)


