from src.Board.Square.chess_square_view import ChessSquareView


class ChessBoard:

    def __init__(self, knight, endpoint):
        self.__board = [[0] * 8 for i in range(8)]
        self.__initialise_board()
        self.__knight = knight
        self.__endpoint = endpoint

    def __initialise_board(self):
        for horizontal in range(0, 8):
            for vertical in range(0, 8):
                self.__board[horizontal][vertical] = ChessSquareView(self,horizontal, vertical)

    def get_board(self):
        return self.__board

    def initial_knight(self):
        self.__board[0][0].place_knight()

    def change_endpoints(self,position):
        horizonal_endpoint = self.__endpoint.get_position()["x_coordinate"]
        vertical_endpoint = self.__endpoint.get_position()["y_coordinate"]

        if horizonal_endpoint is not None and vertical_endpoint is not None:
            self.__board[horizonal_endpoint][vertical_endpoint].remove_endpoint()

        self.__endpoint.set_position(position["x_coordinate"],position["y_coordinate"])
    
    def change_knight_position(self,position):
        horizonal_knight_position = position["x_coordinate"]
        vertical_knight_position = position["y_coordinate"]

        self.__board[ horizonal_knight_position][vertical_knight_position].remove_knight()
