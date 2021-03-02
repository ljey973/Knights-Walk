import tkinter as tk
from src.Algorithms.Endpoint.endpoint import Endpoint
from src.Algorithms.BFS.bfs_button import BFSButton
from src.Board.chess_board import ChessBoard
from src.Piece.knight import Knight
from src.Algorithms.DFS.dfs_button import DFSButton
from src.Algorithms.Dijkstra.dijkstra_button import DijkstraButton
from src.Help.help_button import HelpButton


def main():
    window = tk.Tk()
    window.title("Knight's Walk")
    knight = Knight(0, 0)
    endpoint = Endpoint(None,None)
    board = ChessBoard(knight,endpoint)
    board.initial_knight()
    BFSButton(knight,endpoint,board)
    DFSButton(knight,endpoint,board)
    DijkstraButton(knight,endpoint,board)
    HelpButton()
    window.mainloop()


if __name__ == "__main__":
    main()
