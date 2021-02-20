class Node():

    def __init__(self, x, y, parent):
        self.__x = x
        self.__y = y
        self.__parent = parent

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_parent(self):
        return self.__parent