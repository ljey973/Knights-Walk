from PIL import Image, ImageTk


class Knight:

    def __init__(self, x_coordinate, y_coordinate):
        self.__position = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate
        }
        self.__knight_image = self.__knight_image()
        self.__movement = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1))

    def __knight_image(self):
        return ImageTk.PhotoImage(Image.open('src/Piece/knight.png'))

    def get_position(self):
        return self.__position

    def set_position(self, x_coordinate, y_coordinate):
        self.__position = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate
        }

    def return_image(self):
        return self.__knight_image

    def get_movement(self):
        return self.__movement
