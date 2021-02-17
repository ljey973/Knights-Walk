from src.Board.Square.colour_enum import Colour
from tkinter import Frame, Button, PhotoImage
from src.Piece.knight import Knight



class ChessSquareView(Frame):

    def __init__(self, x_coordinate, y_coordinate, square_model):
        super().__init__()
        self.__rectangle_positions = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
        }
        self.__colour = None
        self.__square_model = square_model
        self.__determine_colour()
        self.draw_square()


    def draw_square(self):
        image = Knight(0, 0).return_image()
        B = Button(width=50, height=50, bg=self.__colour,image = image)
        B.image = image
        B.grid(row=self.__rectangle_positions["x_coordinate"], column=self.__rectangle_positions["y_coordinate"])
        self.grid(row=self.__rectangle_positions["x_coordinate"], column=self.__rectangle_positions["y_coordinate"])

    def __determine_colour(self):
        if self.__rectangle_positions["x_coordinate"] % 2 == 1 and self.__rectangle_positions["y_coordinate"] % 2 == 0:
            self.__colour = Colour.WHITE.value
        elif self.__rectangle_positions["x_coordinate"] % 2 == 0 and self.__rectangle_positions["y_coordinate"] % 2 == 1:
            self.__colour = Colour.WHITE.value
        else:
            self.__colour = Colour.BLACK.value


