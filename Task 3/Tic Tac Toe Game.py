def print_board(board):
    try:
        for row in board:
            print(" | ".join(row))
            print("---------")
    except Exception as e:
        print(f"Error printing board: {e}")

def check_winner(board, player):
    try:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3)):
            return True
        return False
    except Exception as e:
        print(f"Error checking winner: {e}")
        return False

def is_full(board):
    try:
        return all(cell != " " for row in board for cell in row)
    except Exception as e:
        print(f"Error checking if board is full: {e}")
        return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if not (0 <= row <= 2 and 0 <= col <= 2):
                raise ValueError("Row and column must be between 0 and 2.")

            if board[row][col] != " ":
                print("That cell is already occupied. Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return

            if is_full(board):
                print_board(board)
                print("It's a draw!")
                return

            current_player = "O" if current_player == "X" else "X"

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except IndexError:
            print("Invalid row or column. Please enter numbers between 0 and 2.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    while True:
        try:
            print ("Welcome to Tic Tac Toe Game!")
            print ("1. Start")
            print ("2. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                play_game()
            elif choice== 2:
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()