from src.Algorithms.Nodes.node import Node
from src.Algorithms.abstract_algorithm import AbstractAlgorithm
import queue


class BFSAlgorithm(AbstractAlgorithm):

    def __init__(self, knight, endpoint, board):
        super().__init__(knight,endpoint,board)
        self.__visiting_queue = queue.Queue()

    def calculate_path(self):
        initial_node = Node(self.initial_x, self.initial_y, None)
        self.__visiting_queue.put(initial_node)
        self.visited[self.initial_x][self.initial_y] = True

        while self.__visiting_queue.qsize() > 0:
            current_node = self.__visiting_queue.queue[0]
            self.__visiting_queue.get()

            if current_node.get_x() == self.x_endpoint and current_node.get_y() == self.y_endpoint:
                self.get_path(current_node)
                return

            for i in range(8):
                adjacent_x = current_node.get_x() + self.knight_movement[i][0]
                adjacent_y = current_node.get_y() + self.knight_movement[i][1]

                if self.is_inside_board(adjacent_x, adjacent_y) and not self.visited[adjacent_x][adjacent_y]:
                    self.visited[adjacent_x][adjacent_y] = True
                    self.__visiting_queue.put(Node(adjacent_x, adjacent_y, current_node))
