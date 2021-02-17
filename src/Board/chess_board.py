from src.Board.Square.chess_square_view import ChessSquareView
from src.Board.Square.chess_square_model import ChessSquareModel
from random import randrange


class ChessBoard:

    def __init__(self):
        self.__board = [[0] * 8 for i in range(8)]
        self.__initialise_board()
        self.__initial_horizontal = randrange(9)
        self.__initial_vertical = randrange(9)

    def __initialise_board(self):
        for horizontal in range(0, 8):
            for vertical in range(0, 8):
                self.__board[horizontal][vertical] = ChessSquareView(horizontal, vertical,
                                                                     ChessSquareModel(horizontal, vertical))

    def __initial_knight(self):
        self.__board[0][0]