"""
-----------------------------------------------------------------------------
Name: Maitrey Vivek Phatak
Course: MS in APPLIED DATA SCIENCE
Date: September 28, 2025
Program: TicTacToe 
Overview:
    I am implementing a two-player Tic-Tac-Toe game.It displays a 3x3 board which 
    accepts input as "row,column", validates inputs, and checks for wins across 
    rows/columns/diagonals or a draw on a full board. After each round it offers 
    to start a new game without restarting the program.
-----------------------------------------------------------------------------
"""
from typing import List

Board = List[List[str]]

class TicTacToe:
    def __init__(self):            # Initializing a 3x3 grid of spaces, looping row by row

        
        self.board: Board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(" ")
            self.board.append(row)

        # Starting the first turn as X
        self.turn: str = "X"
        self.sep = "." * 17


    def printBoard(self) -> None:         
        """
        Printing the current board grid.
        """
        print()
        print(self.sep)
        print("|R\\C| 0 | 1 | 2 |")
        print(self.sep)
        for r in range(3):
            print(f"| {r} | {self.board[r][0]} | {self.board[r][1]} | {self.board[r][2]} |")
            print(self.sep)
        print()


    def resetBoard(self) -> None:        # We can reset the board with this function

        self.board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(" ")
            self.board.append(row)
        self.turn = "X"

    def validateEntry(self, row: int, col: int) -> bool:
        """
        This allows us to validate that a proposed move is on the board.
    
        """
        if not (0 <= row <= 2 and 0 <= col <= 2):
            return False
        return self.board[row][col] == " "

    def checkFull(self) -> bool:
        """
        We can check whether the board has any empty spaces remaining.
        Iterate over cells; returns True if none are empty.
    
        """
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == " ":
                    return False
        return True

    def checkWin(self, turn: str) -> bool:     # All winning possibilities are checked for a match
        
        lines = [
            # rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # cols
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        for line in lines:
            all_match = True
            for r, c in line:
                if self.board[r][c] != turn:
                    all_match = False
                    break
            if all_match:
                return True
        return False

    def checkEnd(self, turn: str) -> bool:
        """
        We can evaluate whether the game has ended.
    
        """
        if self.checkWin(turn):
            print(f"{turn} IS THE WINNER!!!")
            print()
            self.printBoard()
            return True
        if self.checkFull():
            print("DRAW! NOBODY WINS!")
            print()
            self.printBoard()
            return True
        return False

    def _promptAndApplyMove(self, player: str) -> None:
        """
        We prompt the current player for a move, validate input, and place the mark.
        Ensures the entry is according to constraints.
        """

        print(f"{player}'s turn.")
        print()
        print(f"Where do you want your {player} placed?")
        print()
        print("Please enter row number and column number separated by a comma.")
        print()

        move_str = input().strip()
        parts = [x.strip() for x in move_str.split(",")]

        if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
            print("Invalid entry: try again.")
            print()
            print("Row & column numbers must be either 0, 1, or 2.")
            print()
            return self._promptAndApplyMove(player)

        r, c = int(parts[0]), int(parts[1])

        print(f"You have entered row #{r}")
        print()
        print(f"and column #{c}")
        print()

        # Bound Check
        if not (0 <= r <= 2 and 0 <= c <= 2):
            print("Invalid entry: try again.")
            print()
            print("Row & column numbers must be either 0, 1, or 2.")
            print()
            return self._promptAndApplyMove(player)

        # Already selected alternative
        if self.board[r][c] != " ":
            print("That cell is already taken.")
            print()
            print("Please make another selection.")
            print()
            return self._promptAndApplyMove(player)

        print("Thank you for your selection.")
        print()
        self.board[r][c] = player

    def play(self):
        """
        Here we run the loop. Start a new game, alternates turns between 'X' and 'O'.

        """
        while True:
            print("New Game: X goes first.")
            print()
            self.resetBoard()
            self.printBoard()

            current = "X"
            while True:
                self._promptAndApplyMove(current)

                # Checking if the game ended 
                if self.checkEnd(current):
                    break

                self.printBoard()
                current = "O" if current == "X" else "X"

            print("Another game? Enter Y or y for yes.")
            again = input().strip()
            if again not in ("Y", "y"):
                print()
                print("Thank you for playing!")
                return



def main():
    """
    Program entrypoint.

    """
    TicTacToe().play()

if __name__ == "__main__":
    main()
