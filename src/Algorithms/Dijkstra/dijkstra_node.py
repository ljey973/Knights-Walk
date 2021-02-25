class DijkstraNode():

    def __init__(self, x, y, parent,distance):
        self.__x = x
        self.__y = y
        self.__parent = parent
        self.__distance = distance

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_parent(self):
        return self.__parent

    def get_distance(self):
        return self.__distance

    def __lt__(self, other):
        return (self.__distance <= other.get_distance())