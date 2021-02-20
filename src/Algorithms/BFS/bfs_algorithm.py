from src.Algorithms.BFS.node import Node
import queue


class BFSAlgorithm:

    def __init__(self, knight, endpoint, board):
        self.__knight = knight
        self.__knight_movement = knight.get_movement()
        self.__endpoint = endpoint
        self.__visited = [[False for i in range(8)]
                          for j in range(8)]
        self.__visiting_queue = queue.Queue()
        self.__path = []
        self.__board = board

    def __is_inside_board(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False

    def __get_path(self, node):
        if node.get_parent() is None:
            self.__path.append((node.get_x(), node.get_y()))
            print(self)
            for node in self.__path:
                self.__board.colour_path(node[0], node[1])
            return
        else:
            self.__path.append((node.get_x(), node.get_y()))
            self.__get_path(node.get_parent())


    def calculate_path(self):
        initial_x = self.__knight.get_position()["x_coordinate"]
        initial_y = self.__knight.get_position()["y_coordinate"]
        x_endpoint = self.__endpoint.get_position()["x_coordinate"]
        y_endpoint = self.__endpoint.get_position()["y_coordinate"]
        initial_node = Node(initial_x, initial_y, None)
        self.__visiting_queue.put(initial_node)
        self.__visited[initial_x][initial_y] = True

        while self.__visiting_queue.qsize() > 0:
            current_node = self.__visiting_queue.queue[0]
            self.__visiting_queue.get()

            if current_node.get_x() == x_endpoint and current_node.get_y() == y_endpoint:
                print("yes")
                self.__get_path(current_node)
                return

            for i in range(8):
                adjacent_x = current_node.get_x() + self.__knight_movement[i][0]
                adjacent_y = current_node.get_y() + self.__knight_movement[i][1]

                if self.__is_inside_board(adjacent_x, adjacent_y) and not self.__visited[adjacent_x][adjacent_y]:
                    self.__visited[adjacent_x][adjacent_y] = True
                    self.__visiting_queue.put(Node(adjacent_x, adjacent_y, current_node))
