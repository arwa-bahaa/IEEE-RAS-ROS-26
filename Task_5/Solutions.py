def print_board(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(board):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return True
    return False

while True:
    board = ["1","2","3","4","5","6","7","8","9"]
    moves = 0

    player = input("Player 1 choose X or O: ").upper()
    while player not in ["X", "O"]:
        player = input("Choose only X or O: ").upper()
    turn = player

    while True:
        move = input("Player " + turn + " choose position (1-9): ")

        if move not in board:
            print("Invalid move! Try again.")
            continue

        board[int(move)-1] = turn
        moves += 1
        print_board(board)

        if check_winner(board):
            print("Player " + turn + " wins!")
            break

        if moves == 9:
            print("Draw!")
            break

        turn = "O" if turn == "X" else "X"
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Game Over")
        break
