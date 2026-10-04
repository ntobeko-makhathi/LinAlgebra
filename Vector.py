class Vector(Matrix):
    def __init__(self, vector):
        super().__init__(vector)
        self.vector = vector
        self.__rows = len(vector)
        self.__columns = 1

    def display(self, operation=None):
        if operation is None:
            print("Vector:")
        else:
            print(f"Vector after {operation}:")
        for row in self.vector:
            print(row)