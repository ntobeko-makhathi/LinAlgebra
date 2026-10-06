import Matrix
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
    def matrix_multiply(self, matrix):
        if self.__columns != matrix.get_rows():
            raise ValueError("Incompatible dimensions for multiplication.")
        result = []
        for i in range(self.__rows):
            sum_product = 0
            for j in range(matrix.get_columns()):
                sum_product += self.vector[i][0] * matrix.get_element(j, 0)
            result.append([sum_product])
        return Vector(result)