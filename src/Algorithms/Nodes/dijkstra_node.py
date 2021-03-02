from src.Algorithms.Nodes.abstract_node import AbstractNode

class DijkstraNode(AbstractNode):

    def __init__(self, x, y, parent,distance):
        super().__init__(x, y, parent)
        self.__distance = distance

    def get_distance(self):
        return self.__distance

    def __lt__(self, other):
        return (self.__distance <= other.get_distance())