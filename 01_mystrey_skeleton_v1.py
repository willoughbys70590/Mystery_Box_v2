from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        #Mystrey Heading (row 0)
        self .mystrey_box_label = Label(sellf.start_frame, text="Mystrey Box Game",
                                        font="Arial 19 bold")
        self.mystrey_box_label.grid(row=1)

        #Entry box... (row 1)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=2)

        #Play Button (row 2)
        self.lowstakes_button = Button(text="Low ($5)",
                                       comand=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=2, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)

    def Game:
        def __init__(self, parent, stake, starting_balance):
            print(stake)
            print(starting_balance)

            partner.lowestakes_button.config(state=DISABLED)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystrey Box Game")
    something = start(root)
    root.mainloop()


