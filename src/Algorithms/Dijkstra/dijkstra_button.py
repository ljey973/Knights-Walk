from tkinter import Frame, Button
from src.Algorithms.Dijkstra.dijkstra_algorithm import DijkstrasAlgorithm


class DijkstraButton(Frame):

    def __init__(self,knight,endpoint,board):
        super().__init__()
        self.__knight = knight
        self.__endpoint = endpoint
        self.__board = board
        self.__button = Button(width=5, height=1,bg="blue",command=self.initiate_dijkstra_algorithm)
        self.__button.grid(row=9, column=2)
        self.grid(row=9, column=2)

    def initiate_dijkstra_algorithm(self):
        DijkstrasAlgorithm(self.__knight,self.__endpoint,self.__board).dijkstra_initiator()