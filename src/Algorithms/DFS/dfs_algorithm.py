from src.Algorithms.abstract_algorithm import AbstractAlgorithm


class DFSAlgorithm(AbstractAlgorithm):

    def __init__(self, knight, endpoint, board):
        super().__init__(knight, endpoint, board)
        self.__stack_path = []

    def calculate_path(self):
        self.__dfs_helper(self.initial_x, self.initial_y)

    def __get_path(self):
        self.board.colour_path(self.__stack_path)

    def __dfs_helper(self, x_coordinate, y_coordinate):
        self.visited[x_coordinate][y_coordinate] = True
        self.__stack_path.append((x_coordinate, y_coordinate))

        if x_coordinate == self.x_endpoint and y_coordinate == self.y_endpoint:
            self.__get_path()
            return

        for i in range(8):
            adjacent_x = x_coordinate + self.knight_movement[i][0]
            adjacent_y = y_coordinate + self.knight_movement[i][1]

            if self.is_inside_board(adjacent_x, adjacent_y) and not self.visited[adjacent_x][adjacent_y]:
                self.__dfs_helper(adjacent_x, adjacent_y)
        #   Since the element has no valid moves, remove it from the list(since it's the top element) and backtrack to last node
        self.__stack_path.pop()
