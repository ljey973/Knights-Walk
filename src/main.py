import tkinter as tk
from src.Board.chess_board import ChessBoard
from src.Piece.knight import Knight


def main():
    window = tk.Tk()
    ChessBoard()
    Knight(0,0)
    window.mainloop()


if __name__ == "__main__":
    main()
