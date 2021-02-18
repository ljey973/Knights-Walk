import tkinter as tk
from src.Algorithms.Endpoint.endpoint import Endpoint
from src.Board.chess_board import ChessBoard
from src.Piece.knight import Knight


def main():
    window = tk.Tk()
    knight = Knight(0, 0)
    endpoint = Endpoint(None,None)
    ChessBoard(knight,endpoint).initial_knight()
    window.mainloop()


if __name__ == "__main__":
    main()
