class Endpoint:

    def __init__(self, x_coordinate, y_coordinate):
        self.__position = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate
        }

    def get_position(self):
        return self.__position

    def set_position(self, x_coordinate, y_coordinate):
        self.__position = {
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate
        }
