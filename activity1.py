#Designing a tic-tac-toe game with AI as player 2
import random
print("Welcome to the Tic-Tac_toe game!")
print("You are player 1 and will play with 'X'. The AI is player 2 and will play with 'O'.")
print("What is your name?")
name = input("")
print(f"Hello {name}! Let's begin!")
def print_board(board: dict[int, str]) -> None:
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[7]} | {board[8]} | {board[9]}")
board: dict[int, str] = {i: f"{i}" for i in range(1, 10)}
print_board(board)
keys = list(board.keys())
number_of_moves = 0
while True:
    print("Which position on the board would you like to place your 'X'? (1-9)")
    position = int(input(""))
    if position in keys:
        board[position] = 'X'
        print_board(board)
        number_of_moves += 1
    computer_move = random.choice([key for key in keys if board[key] not in ['X', 'O']])
    board[computer_move] = 'O'
    print(f"AI places its 'O' in position {computer_move}")
    print_board(board)
    number_of_moves += 1
    if number_of_moves >= 5:
        if (board[1] == board[2] == board[3] == 'X') or (board[4] == board[5] == board[6] == 'X') or (board[7] == board[8] == board[9] == 'X') or (board[1] == board[4] == board[7] == 'X') or (board[2] == board[5] == board[8] == 'X') or (board[3] == board[6] == board[9] == 'X') or (board[1] == board[5] == board[9] == 'X') or (board[3] == board[5] == board[7] == 'X'):
            print(f"Congratulations {name}, you have won!")
            break
        if (board[1] == board[2] == board[3] == 'O') or (board[4] == board[5] == board[6] == 'O') or (board[7] == board[8] == board[9] == 'O') or (board[1] == board[4] == board[7] == 'O') or (board[2] == board[5] == board[8] == 'O') or (board[3] == board[6] == board[9] == 'O') or (board[1] == board[5] == board[9] == 'O') or (board[3] == board[5] == board[7] == 'O'):
            print("AI has won! Better luck next time.")
            break
    if number_of_moves == 9:
        print("It's a tie!")
        break