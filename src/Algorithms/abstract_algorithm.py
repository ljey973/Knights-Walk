from abc import ABC
from src.Algorithms.Nodes import node


class AbstractAlgorithm(ABC):

    def __init__(self, knight, endpoint, board):
        self.initial_x = knight.get_position()["x_coordinate"]
        self.initial_y = knight.get_position()["y_coordinate"]
        self.x_endpoint = endpoint.get_position()["x_coordinate"]
        self.y_endpoint = endpoint.get_position()["y_coordinate"]
        self.knight_movement = knight.get_movement()
        self.visited = [[False for i in range(8)]
                          for j in range(8)]
        self.path = []
        self.board = board

    def is_inside_board(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False

    def get_path(self, node):
        if node.get_parent() is None:
            self.path.append((node.get_x(), node.get_y()))
            self.board.colour_path(self.path)
            return
        else:
            self.path.append((node.get_x(), node.get_y()))
            self.get_path(node.get_parent())

    def __get_path(self):
        if node.get_parent() is None:
            self.__path.append((node.get_x(), node.get_y()))
            self.__board.colour_path(self.__path)
            return
        else:
            self.__path.append((node.get_x(), node.get_y()))
            self.__get_path(node.get_parent())
