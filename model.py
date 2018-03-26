from scipy.sparse import coo_matrix
import numpy as np

class UserInput:
    __data = np.zeros((1280, 720), dtype=bool)

    def draw(self, x, y):
        self.__data[x][y] = True

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)