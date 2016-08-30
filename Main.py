from tkinter import *
from Square import Square
from NumberButton import NumberButton
import os


class SudokuSolver(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.squares = [[Square(self) for i in range(9)] for j in range(9)]
        self.init_squares()
        self.number_button = [NumberButton] * 9
        self.init_number_button()
        self.solver_button = Button(self, text="Solve", command=self.solve)
        self.reset_button = Button(self, text="Reset", command=self.reset)
        self.init_function_button()
        self.load_from_file()

    # Init 9x9 squares
    def init_squares(self):
        for i in range(9):
            for j in range(9):
                self.squares[i][j].grid(row=i, column=j)

    # Init number buttons 1->9
    def init_number_button(self):
        for i in range(9):
            self.number_button[i] = NumberButton(self, i)
            self.number_button[i].grid(row=11, column=i)

    # Init Solve and Reset button
    def init_function_button(self):
        self.solver_button.grid(row=12, column=0, columnspan=3, sticky=E + W)
        self.reset_button.grid(row=12, column=6, columnspan=3, sticky=E + W)

    # Load data from file
    def load_from_file(self):
        f = open(os.getcwd() + '\\2.sdk', 'r')
        present = 0
        for i in range(9):
            for j in range(9):
                f.seek(present)
                if j < 8:
                    present += 2
                else:
                    present += 3
                num = f.read(1)
                if num != '0':
                    self.squares[i][j].set_root(int(num) - 1, True)
        f.close()

    # Solver
    def solve(self):

        # Check each square
        for i in range(9):
            for j in range(9):

                # Solved squares
                if self.squares[i][j].possibles_count == 1:

                    # Save the root of this square
                    root = self.squares[i][j].get_root()

                    # Remove the possibility of this root in other square
                    #  which in the same row or column with this
                    for k in range(9):
                        if k != j:
                            self.squares[i][k].remove_possible(root)
                        if k != i:
                            self.squares[k][j].remove_possible(root)

                    # Also in  the the block
                    m = int(i / 3)
                    n = int(j / 3)
                    for k in range(1, 4):
                        for l in range(1, 4):
                            r = (m + 1) * 3 - k
                            c = (n + 1) * 3 - l
                            if r != i | c != j:
                                self.squares[r][c].remove_possible(root)
                else:
                    # Unsolved squares

                    # With each possible of root check if this square is the only
                    # one which has the possible in the row or column
                    for k in range(9):
                        if self.squares[i][j].possibles[k] == 1:
                            exist = False
                            for l in range(9):
                                if l != i:
                                    if self.squares[l][j].possibles[k] == 1:
                                        exist = True
                                        break
                            if not exist:
                                self.squares[i][j].set_root(k)
                                break
                            exist = False
                            for l in range(9):
                                if l != j:
                                    if self.squares[i][l].possibles[k] == 1:
                                        exist = True
                                        break
                            if not exist:
                                self.squares[i][j].set_root(k)
                                break

                    # Also in block
                    # There are error somewhere blow
                                
                            m = int(i / 3)
                            n = int(j / 3)
                            exist = False
                            for t in range(1, 4):
                                for l in range(1, 4):
                                    r = (m + 1) * 3 - t
                                    c = (n + 1) * 3 - l
                                    if r != i | c != j:
                                        if self.squares[r][c].possibles[k] == 1:
                                            exist = True
                                            break
                                if exist:
                                    break
                            if not exist:
                                self.squares[i][j].set_root(k)
                                break

    # Reset the game
    def reset(self):
        for i in range(9):
            for j in range(9):
                self.squares[i][j].reset()

    # Get number of solved squares
    def get_solve(self):
        solved = 0
        for i in range(9):
            for j in range(9):
                if self.squares[i][j].possibles_count == 1:
                    solved += 1
        return solved


mainWindow = Tk()
mainWindow.title("Sudoku Solver")
app = SudokuSolver(mainWindow)
mainWindow.mainloop()
