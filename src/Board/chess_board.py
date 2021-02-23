from src.Board.Square.chess_square_view import ChessSquareView


class ChessBoard:

    def __init__(self, knight, endpoint):
        self.__board = [[0] * 8 for i in range(8)]
        self.__initialise_board()
        self.__knight = knight
        self.__endpoint = endpoint
        self.__num_clicked = 0
        self.__coloured_path = []

    def __initialise_board(self):
        for horizontal in range(0, 8):
            for vertical in range(0, 8):
                self.__board[horizontal][vertical] = ChessSquareView(self,horizontal, vertical,False)

    def get_board(self):
        return self.__board

    def initial_knight(self):
        self.__board[0][0].place_knight()

    def change_endpoints(self,position):
        self.__remove_path()
        horizonal_endpoint = self.__endpoint.get_position()["x_coordinate"]
        vertical_endpoint = self.__endpoint.get_position()["y_coordinate"]

        if horizonal_endpoint is not None and vertical_endpoint is not None:
            self.__board[horizonal_endpoint][vertical_endpoint].remove_endpoint()

        self.__endpoint.set_position(position["x_coordinate"],position["y_coordinate"])

    def change_knight_position(self,position):
        self.__remove_path_knight()
        horizontal_knight_position = self.__knight.get_position()["x_coordinate"]
        vertical_knight_position = self.__knight.get_position()["y_coordinate"]

        self.__board[horizontal_knight_position][vertical_knight_position].remove_knight()
        self.__board[position["x_coordinate"]][position["y_coordinate"]].place_knight()
        self.__knight.set_position(position["x_coordinate"], position["y_coordinate"])

    def increment_num_clicked(self):
        self.__num_clicked +=1

    def reset_num_clicked(self):
        self.__num_clicked = 0

    def get_num_clicked(self):
        return self.__num_clicked

    def colour_path(self,path):
        for node in path:
            self.__board[node[0]][node[1]].change_colour()
            self.__coloured_path.append((node[0],node[1]))

    def __remove_path(self):
        if len(self.__coloured_path) != 0:
            for node in self.__coloured_path:
                self.__board[node[0]][node[1]].remove_endpoint()

        self.__coloured_path.clear()

    def __remove_path_knight(self):
        if len(self.__coloured_path) != 0:
            for node in self.__coloured_path:
                #Remove the blue colour of the path
                if node[0] != self.__endpoint.get_position()["x_coordinate"] or node[1] != self.__endpoint.get_position()["y_coordinate"]:
                    self.__board[node[0]][node[1]].remove_endpoint()
                    #Re-colour the endpoint to red
                else:
                    self.__board[node[0]][node[1]].change_endpoint_colour()

        self.__coloured_path.clear()



