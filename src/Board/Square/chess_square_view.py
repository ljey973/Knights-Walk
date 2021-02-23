from src.Board.Square.colour_enum import Colour
from tkinter import Frame, Button, PhotoImage
from src.Piece.knight import Knight


class ChessSquareView(Frame):

    def __init__(self, chess_board, x_coordinate, y_coordinate,knight_flag):
        super().__init__()
        self.__rectangle_positions = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
        }
        self.__board = chess_board
        self.__colour = self.__determine_colour()
        self.__square = self.draw_square()
        self.__is_knight_present = knight_flag

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
        if self.__is_knight_present is True:
            self.__board.increment_num_clicked()

        elif self.__board.get_num_clicked() >= 1:
            self.__board.change_knight_position(self.__rectangle_positions)
            self.__board.reset_num_clicked()

        else:
            self.__board.change_endpoints(self.__rectangle_positions)
            self.change_endpoint_colour()

    def remove_endpoint(self):
        self.__square.config(bg=self.__colour)

    def place_knight(self):
        image = Knight(0, 0).return_image()
        self.__square.config(image=image)
        self.__square.image = image
        self.set_knight_flag(True)

    def remove_knight(self):
        self.__square.config(image=self.pixel)
        self.set_knight_flag(False)

    def get_position(self):
        return self.__rectangle_positions

    def set_knight_flag(self,knight_flag):
        self.__is_knight_present = knight_flag

    def change_colour(self):
        self.__square.config(bg="blue")

    def change_endpoint_colour(self):
        self.__square.config(bg="red")
