from tkinter import Frame, Button
from src.Algorithms.BFS.bfs_algorithm import BFSAlgorithm


class BFSButton(Frame):

    def __init__(self,knight,endpoint,board):
        super().__init__()
        self.__knight = knight
        self.__endpoint = endpoint
        self.__board = board
        self.__button = Button(width=5, height=1,bg="white",command=self.initiate_bfs_algorithm,text="BFS")
        self.__button.grid(row=9, column=0)
        self.grid(row=9, column=0)

    def initiate_bfs_algorithm(self):
        BFSAlgorithm(self.__knight,self.__endpoint,self.__board).calculate_path()
