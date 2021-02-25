import heapq
from collections import defaultdict
from src.Algorithms.Dijkstra.dijkstra_node import DijkstraNode


class DijkstrasAlgorithm:

    def __init__(self, knight, endpoint, board):
        self.__initial_x = knight.get_position()["x_coordinate"]
        self.__initial_y = knight.get_position()["y_coordinate"]
        self.__x_endpoint = endpoint.get_position()["x_coordinate"]
        self.__y_endpoint = endpoint.get_position()["y_coordinate"]
        self.__knight_movement = knight.get_movement()
        self.__visited = [[False for i in range(8)]
                          for j in range(8)]
        self.__min_heap = []
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
            self.__board.colour_path(self.__path)
            return
        else:
            self.__path.append((node.get_x(), node.get_y()))
            self.__get_path(node.get_parent())

    def dijkstra_initiator(self):
        initial_node = DijkstraNode(self.__initial_x, self.__initial_y, None, 0)
        heapq.heappush(self.__min_heap, initial_node)
        self.__visited[self.__initial_x][self.__initial_y] = True
        self.__dijkstra()

    def __dijkstra(self):
        while len(self.__min_heap) > 0:
            current_node = heapq.heappop(self.__min_heap)
            current_cost = current_node.get_distance()

            if current_node.get_x() == self.__x_endpoint and current_node.get_y() == self.__y_endpoint:
                self.__get_path(current_node)
                return

            for i in range(8):
                adjacent_x = current_node.get_x() + self.__knight_movement[i][0]
                adjacent_y = current_node.get_y() + self.__knight_movement[i][1]

                if self.__is_inside_board(adjacent_x, adjacent_y) and not self.__visited[adjacent_x][adjacent_y]:
                    new_cost = current_cost + 1
                    new_node = DijkstraNode(adjacent_x, adjacent_y, current_node, new_cost)
                    self.__visited[adjacent_x][adjacent_y] = True
                    heapq.heappush(self.__min_heap, new_node)
