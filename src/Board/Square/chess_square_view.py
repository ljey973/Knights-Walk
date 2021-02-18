from src.Board.Square.colour_enum import Colour
from tkinter import Frame, Button, PhotoImage
from src.Piece.knight import Knight


class ChessSquareView(Frame):

    def __init__(self, chess_board, x_coordinate, y_coordinate):
        super().__init__()
        self.__rectangle_positions = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
        }
        self.__board = chess_board
        self.__colour = self.__determine_colour()
        self.__square = self.draw_square()
        self.__num_clicked = 0

    def draw_square(self):
        self.pixel = PhotoImage(width=1, height=1)
        But = Button(width=50, height=50, bg=self.__colour, image=self.pixel, command=self.change_endpoint)
        But.grid(row=self.__rectangle_positions["x_coordinate"], column=self.__rectangle_positions["y_coordinate"])
        self.grid(row=self.__rectangle_positions["x_coordinate"], column=self.__rectangle_positions["y_coordinate"])
        return But

    def __determine_colour(self):
        if self.__rectangle_positions["x_coordinate"] % 2 == 1 and self.__rectangle_positions["y_coordinate"] % 2 == 0:
            return Colour.WHITE.value
        elif self.__rectangle_positions["x_coordinate"] % 2 == 0 and self.__rectangle_positions[
            "y_coordinate"] % 2 == 1:
            return Colour.WHITE.value
        else:
            return Colour.BLACK.value

    def change_endpoint(self):
        if self.__piece is not None:
            self.__num_clicked += 1

        elif self.__num_clicked >= 1:
            self.__board.change_change_knight_position(self.__rectangle_positions)
            self.__num_clicked = 0
        else:
            self.__square.config(bg="red")
            self.__board.change_endpoints(self.__rectangle_positions)

    def remove_endpoint(self):
        self.__square.config(bg=self.__colour)

    def place_knight(self):
        image = Knight(0, 0).return_image()
        self.__square.config(image=image)
        self.__square.image = image

    def remove_knight(self):
        self.__square.config(image=self.pixel)

    def get_position(self):
        return self.__rectangle_positions
