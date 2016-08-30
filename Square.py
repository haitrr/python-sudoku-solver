from tkinter import *


class Square(Button):
    selecting_square = None

    def __init__(self, master):
        Button.__init__(self, master, command=self.on_click, width=3, height=1)
        self.possibles = [1] * 9
        self.possibles_count = 9

    # Check if a number is possible in this square
    def check_possible(self, x):
        if self.possibles[x] == 1:
            return True
        return False

    # Reset the square
    def reset(self):
        self.possibles = [1] * 9
        self.possibles_count = 9
        self.update_label()
        self.configure(text="", bg=self.master.cget('bg'))

    # Set number to Square
    def set_root(self, x, init=False):
        for i in range(9):
            if i == x:
                self.possibles[i] = 1
            else:
                self.possibles[i] = 0
        self.possibles_count = 1
        self.update_label(init)

    # Update label to display number
    def update_label(self, init=False):
        if self.possibles_count == 1:
            for i in range(9):
                if self.possibles[i] == 1:
                    self.configure(text=i + 1, bg='green')
                    if init:
                        self.configure(bg='gray')
        else:
            self.configure(text=self.possibles_count, bg='yellow')

    # Get root of this square in case it is solved
    def get_root(self):
        if self.possibles_count == 1:
            for i in range(9):
                if self.possibles[i] == 1:
                    return i
        return -1

    # Remove a number from possible
    def remove_possible(self, x):
        if self.possibles_count > 1:
            if self.possibles[x] == 1:
                self.possibles[x] = 0
                self.possibles_count -= 1
                self.update_label()

    # Click action
    def on_click(self):
        if Square.selecting_square is self:
            self.set_un_select()
        elif Square.selecting_square is not None:
            Square.selecting_square.setUnSelect()
            self.set_select()
        else:
            self.set_select()

    # set button on select
    def set_select(self):
        self.configure(bg='cyan')
        Square.selectingSquare = self

    # Un_select button
    def set_un_select(self):
        self.configure(bg=self.master.cget('bg'))
        Square.selectingSquare = None
