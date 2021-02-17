
class ChessSquareModel():

    def __init__(self, x_coordinate, y_coordinate):
        self.__position = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate
        }
        self.__isKnightPresent = None

