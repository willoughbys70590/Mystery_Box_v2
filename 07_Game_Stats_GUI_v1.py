from tkinter import *
from functools import partial  # To prevent unwanted windows

import random

class Game:
    def __init__(self):

        # Formatting Variables...
        self.game_stats_list = [50, 6]

        # In actual program this is blank and is populated with user calculations
        self.round_stats_list = ['silver ($4) | silver ($4) | lead($0) - Cost: $10'
                                'lead ($0) | silver ($4) | gold ($10) - Cost: $10'
                                'lead ($0) | lead ($0) | copper ($2) - Cost: $10'
                                'copper ($2) | lead ($0) | copper ($2) - Cost: $10'
                                'lead ($0) | lead ($0) | lead ($0) - Cost: $10'
                                'lead ($0) | lead ($0) | silver ($4) - Cost: $10'
                                'silver ($4) | silver ($4) | silver ($4) - Cost: $10'
                                'copper ($2) | silver ($4) | lead ($0) - Cost: $10'
                                'lead ($0) | lead ($0) | copper ($2) - Cost: $10'
                                'copper ($2) | copper ($2) | silver ($4) - Cost: $10'
                                'copper ($2) | silver ($4) | silver ($4) - Cost: $10'
                                'copper ($2) | lead ($0) | silver ($4) - Cost: $10']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", )



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()