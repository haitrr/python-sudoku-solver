from tkinter import Button
from Square import Square


class NumberButton(Button):
    def __init__(self, master, number):
        self.number = number
        Button.__init__(self, master, text=number + 1, command=self.on_click, width=3, height=1)

    # Click event
    def on_click(self):
        # Set number to selected square
        if Square.selecting_square is not None:
            Square.selecting_square.setRoot(self.number, True)
            Square.selecting_square.set_un_select()
