import heapq
from src.Algorithms.Nodes.dijkstra_node import DijkstraNode
from src.Algorithms.abstract_algorithm import AbstractAlgorithm


class DijkstrasAlgorithm(AbstractAlgorithm):

    def __init__(self, knight, endpoint, board):
        super().__init__(knight, endpoint, board)
        self.__min_heap = []

    def dijkstra_initiator(self):
        initial_node = DijkstraNode(self.initial_x, self.initial_y, None, 0)
        heapq.heappush(self.__min_heap, initial_node)
        self.visited[self.initial_x][self.initial_y] = True
        self.__dijkstra()

    def __dijkstra(self):
        while len(self.__min_heap) > 0:
            current_node = heapq.heappop(self.__min_heap)
            current_cost = current_node.get_distance()

            if current_node.get_x() == self.x_endpoint and current_node.get_y() == self.y_endpoint:
                self.get_path(current_node)
                return

            for i in range(8):
                adjacent_x = current_node.get_x() + self.knight_movement[i][0]
                adjacent_y = current_node.get_y() + self.knight_movement[i][1]

                if self.is_inside_board(adjacent_x, adjacent_y) and not self.visited[adjacent_x][adjacent_y]:
                    new_cost = current_cost + 1
                    new_node = DijkstraNode(adjacent_x, adjacent_y, current_node, new_cost)
                    self.visited[adjacent_x][adjacent_y] = True
                    heapq.heappush(self.__min_heap, new_node)
