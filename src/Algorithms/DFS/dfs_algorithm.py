class DFSAlgorithm:

    def __init__(self, knight, endpoint, board):
        self.__knight = knight
        self.__knight_movement = knight.get_movement()
        self.__visited = [[False for i in range(8)]
                          for j in range(8)]
        self.__stack_path = []
        self.__board = board
        self.__x_endpoint = endpoint.get_position()["x_coordinate"]
        self.__y_endpoint = endpoint.get_position()["y_coordinate"]

    def __is_inside_board(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        else:
            return False

    def calculate_path(self):
        initial_x = self.__knight.get_position()["x_coordinate"]
        initial_y = self.__knight.get_position()["y_coordinate"]
        self.dfs(initial_x,initial_y)

    def __get_path(self):
        self.__board.colour_path(self.__stack_path)

    def dfs(self,x_coordinate,y_coordinate):
        self.__visited[x_coordinate][y_coordinate] = True
        self.__stack_path.append((x_coordinate, y_coordinate))

        if x_coordinate == self.__x_endpoint and y_coordinate == self.__y_endpoint:
            self.__get_path()
            return

        for i in range(8):
            adjacent_x = x_coordinate + self.__knight_movement[i][0]
            adjacent_y = y_coordinate + self.__knight_movement[i][1]

            if self.__is_inside_board(adjacent_x, adjacent_y) and not self.__visited[adjacent_x][adjacent_y]:
                self.dfs(adjacent_x,adjacent_y)
#   Since the element has no valid moves, remove it from the list(since it's the top element) and backtrack to last node
        self.__stack_path.pop()
