"""
-----------------------------------------------------------------------------
Name: Maitrey Vivek Phatak
Course: MS in APPLIED DATA SCIENCE
Date: September 28, 2025
Program: Connect Four
Overview:
    I am implementing a two-player Connect Four game on a 6x7 grid. Players enter
    moves as "<column><row>", the program validates inputs, places 'X'/'O', 
    and checks for wins across rows, columns, and both diagonals or a draw 
    on a full board. After each round it offers to start a new game without restarting the program.
-----------------------------------------------------------------------------
"""
ROWS, COLS = 6, 7
COL_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def resetBoard():
    """
    We can reset the entire board and start from scratch.
    """
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def printBoard(board):       # Printing rows here
    
    for display_r in range(ROWS, 0, -1):
        r = display_r - 1
        line = f"| {display_r} |"
        for c in range(COLS):
            line += f" {board[r][c]} |"
        print(line)

    footer = "|R/C|"
    for ch in COL_LETTERS:
        footer += f" {ch} |"
    print(footer)
    print()

def next_empty_row(board, col_idx):
    """
    We can use the function to find the lowest available index in the given column.

    """
    for r in range(ROWS):
        if board[r][col_idx] == " ":
            return r
    return None

def parse_choice(s):    # Parsing the user entered option.

    s = s.strip().lower()
    if len(s) < 2:
        return None, None
    col = s[0]
    if col not in COL_LETTERS:
        return None, None
    try:
        row = int(s[1:])
    except ValueError:
        return None, None
    return col, row

def validateEntry(board, col, row):   # We can validate whether a move is allowed 
    

    if col not in COL_LETTERS:
        return False
    if not (1 <= row <= ROWS):
        return False

    column_index = COL_LETTERS.index(col)
    r_target = row - 1  # internal index
    next_r = next_empty_row(board, column_index)
    if next_r is None:
        return False  # column full
    if next_r != r_target:
        return False  # We must pick the lowest available cell in that column
    if board[r_target][column_index] != " ":
        return False
    return True

def place_token(board, col, row, token):

    column_index = COL_LETTERS.index(col)
    row_index = row - 1
    board[row_index][column_index] = token

def checkFull(board):
    """
    I am using the following funciton to determine whether the board has no available moves.

    """
    for c in range(COLS):
        if board[ROWS - 1][c] == " ":
            if next_empty_row(board, c) is not None:
                return False

    for c in range(COLS):
        if next_empty_row(board, c) is not None:
            return False
    return True

def availablePosition(board):        # Next valid moves available.
    
    positions = []
    for c_index_, ch in enumerate(COL_LETTERS):
        r = next_empty_row(board, c_index_)
        if r is not None:
            positions.append(f"{ch}{r+1}")
    return positions

def checkWin(board, turn):
    """
    We can check for a win by the specified token.
    The code scans horizontally, vertically, and along both diagonals for win chance. 

    """
    t = turn

    # Horizontal
    for r in range(ROWS):
        count = 0
        for c in range(COLS):
            if board[r][c] == t:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0

    # Vertical
    for c in range(COLS):
        count = 0
        for r in range(ROWS):
            if board[r][c] == t:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0

    # Diagonal 
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != t:
                continue
            # walk down-right up to 3 more steps
            cnt = 1
            rr, cc = r + 1, c + 1
            while rr < ROWS and cc < COLS and board[rr][cc] == t:
                cnt += 1
                if cnt >= 4:
                    return True
                rr += 1; cc += 1

    # Diagonal 
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != t:
                continue
            cnt = 1
            rr, cc = r + 1, c - 1  # because our internal row 0 is the bottom
            while rr < ROWS and cc >= 0 and board[rr][cc] == t:
                cnt += 1
                if cnt >= 4:
                    return True
                rr += 1; cc -= 1

    return False

def checkEnd(board, turn):

    if checkWin(board, turn):
        return True
    if checkFull(board):
        return True
    return False

# Game loop Interface

def play_game():
    """
    Starting a new game with 'X' first, displaying the board, validating the selection, 
    placing the token, checking for win, and alternating turns.

    """
    while True:
        board = resetBoard()
        current = "X"
        print("New game: X goes first.\n")
        printBoard(board)

        while True:
            print(f"{current}'s turn.")
            print(f"Where do you want your {current} placed?")
            avail = availablePosition(board)
            print(f"Available positions are: {avail}\n")

            choice = input("Please enter column-letter and row-number (e.g., a1): ")
            col, row = parse_choice(choice)
            if col is None:
                print("\nInvalid input format. Try again (e.g., a1).\n")
                continue

            if not validateEntry(board, col, row):
                print("\nInvalid selection (out of range, column full, or not the lowest spot). Try again.\n")
                continue

            place_token(board, col, row, current)
            print("\nThank you for your selection.\n")
            printBoard(board)

            # Check end conditions 
            if checkWin(board, current):
                print(f"{current} IS THE WINNER!!!\n")
                break
            if checkFull(board):
                print("It's a draw.\n")
                break

            # Swap turns
            current = "O" if current == "X" else "X"

        # ask to play again
        again = input("Another game (y/n)? ").strip().lower()
        print()
        if not again or again[0] != 'y':
            print("Thank you for playing!")
            return


if __name__ == "__main__":
    play_game()
