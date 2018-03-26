from scipy.sparse import coo_matrix

class UserInput:
    __data = []
    def __init__(self):
        for x in range(0,1280):
            self.__data.append([])
            for y in range(0,720):
                self.__data[x].append(False)

    def draw(self, x, y):
        self.__data[x][y] = True

    def get_data(self):
        return self.__data

    def __str__(self):
        data = coo_matrix(self.__data)
        return str(data.toarray())
        # just because it prints nicely