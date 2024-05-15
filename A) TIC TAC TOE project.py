def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!\n")
    print("[Following are the position of each block\nchoose the number where you want to X or O] \n")
    print_board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
    print("\n")
    print("---Let's Start The Game Now---\n")

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn")

        position = input("Enter position (1-9): ")
        print("\n")

        if not position.isdigit() or not (1 <= int(position) <= 9):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        position = int(position) - 1
        row = position // 3
        col = position % 3

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    tic_tac_toe()
