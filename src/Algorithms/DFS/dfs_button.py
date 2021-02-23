from tkinter import Frame, Button
from src.Algorithms.DFS.dfs_algorithm import DFSAlgorithm


class DFSButton(Frame):

    def __init__(self,knight,endpoint,board):
        super().__init__()
        self.__knight = knight
        self.__endpoint = endpoint
        self.__board = board
        self.__button = Button(width=5, height=1,bg="blue",command=self.initiate_dfs_algorithm)
        self.__button.grid(row=9, column=1)
        self.grid(row=9, column=1)

    def initiate_dfs_algorithm(self):
        DFSAlgorithm(self.__knight,self.__endpoint,self.__board).calculate_path()