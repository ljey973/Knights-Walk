from tkinter import Frame, Button

class HelpButton(Frame):

    def __init__(self):
        super().__init__()
        self.__button = Button(width=5, height=1,bg="white ",text="Help")
        self.__button.grid(row=9, column=7)
        self.grid(row=9, column=7)

