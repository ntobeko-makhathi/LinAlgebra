#auther: @NtobekoMakhathi

class Matrix:
    def __init__(self, matrix=None):
        #This constructor creates a matrix from user input
        self.matrix = self.create() if matrix is None else matrix
        self.__rows = len(self.matrix)
        self.__columns = len(self.matrix[0]) if self.matrix else 0

    @classmethod
    def matrix(cls, matrix): 
            #This constructor creates a matrix from a given list of lists
            mymatrix = matrix
            return cls(mymatrix)

    
    def det(self, m):
        #This function calculates the determinant of a matrix using recursion
        d=0
        if len(m)<1:
            return None
        if not self.is_square():
            print("The matrix is not square, cannot calculate determinant")
            return None
        if len(m)==1:
            return m[0][0]
        else:
            for j in range(len(m[0])):
                minor=[]
                for i in range(1,len(m[0])):
                    minor.append((m[i][:j]+m[i][j+1:]))
        
                d+=m[0][j]*((-1)**(j))*self.det(minor)
                
            return d
    def create(self):
        #This function creates a matrix from user input
        matrix =[]
        row = int(input("How many __rows is the matrix:\n"))
        column = int(input("How many column is the matrix:\n"))

        for i in range(row):
            row_value = []
            print(f"Enter Row {i+1} values one by one:")
            for j in range(column):
                a = int(input(""))
                row_value.append(a)
            matrix.append(row_value)
        return list(matrix)

    def display(self):
        #This function displays the matrix and its determinant
        print("\nmatrix A:\n")
        for rw in self.matrix:
            print(rw)  
        determinant = self.det((self.matrix))  
        print (f"\ndet(A) = {determinant}")

    def add(self, otherMatrix):
        #This function adds two matrices together
        result=[]
        if (self.__rows==otherMatrix.__rows and self.__columns==otherMatrix.__columns):
            for i in range(self.__rows):
                row=[]
                for j in range(self.__columns):
                    row.append(self.matrix[i][j]+otherMatrix.matrix[i][j])
                result.append(row)
            return result
        else:
            print("The matrices are not the same size, cannot add them together")
            return None

    def multiply(self, otherMatrix):
        #This function multiplies two matrices together
        result=[]
        if (self.__columns==otherMatrix.__rows):
            for i in range(self.__rows):
                row=[]
                for j in range(otherMatrix.__columns):
                    sum=0
                    for k in range(self.__columns):
                        sum+=self.matrix[i][k]*otherMatrix.matrix[k][j]
                    row.append(sum)
                result.append(row)
            return result
        else:
            print("The matrices are not compatible for multiplication")
            return None

    def transpose(self):
        #This function transposes a matrix
        result=[]
        for i in range(self.__columns):
            row=[]
            for j in range(self.__rows):
                row.append(self.matrix[j][i])
            result.append(row)
        return result

    def inverse(self):
        #This function calculates the inverse of a matrix using the adjoint method
        if not self.is_invertible():
            print("The matrix is not invertible, cannot calculate inverse")
            return None
        else:
            adjoint=[]
            for i in range(self.__rows):
                row=[]
                for j in range(self.__columns):
                    minor=[]
                    for k in range(self.__rows):
                        if k!=i:
                            minor.append(self.matrix[k][:j]+self.matrix[k][j+1:])
                    row.append(((-1)**(i+j))*self.det(minor))
                adjoint.append(row)
            adjoint=self.transpose(adjoint)
            inverse=[]
            for i in range(self.__rows):
                row=[]
                for j in range(self.__columns):
                    row.append(adjoint[i][j]/self.det(self.matrix))
                inverse.append(row)
            return inverse
    def rank(self):
        #This function calculates the rank of a matrix using row reduction
        matrix=self.matrix
        for i in range(self.__rows):
            for j in range(self.__columns):
                if matrix[i][j]!=0:
                    for k in range(i+1,self.__rows):
                        factor=matrix[k][j]/matrix[i][j]
                        for l in range(j,self.__columns):
                            matrix[k][l]-=factor*matrix[i][l]
                    break
        rank=0
        for i in range(self.__rows):
            if any(matrix[i]):
                rank+=1
        return rank

    def is_square(self):
        #This function checks if a matrix is square
        if self.__rows==self.__columns:
            return True
        else:
            return False

    def is_invertible(self):
        #This function checks if a matrix is invertible
        if not self.is_square():
            print("The matrix is not square, cannot check if it is invertible")
            return False
        det=self.det(self.matrix)
        if det==0:
            return False
        else:
            return True

    def is_symmetric(self):
        #This function checks if a matrix is symmetric
        if not self.is_square():
            print("The matrix is not square, cannot check if it is symmetric")
            return False
        for i in range(self.__rows):
            for j in range(i,self.__columns):
                if self.matrix[i][j]!=self.matrix[j][i]:
                    return False
        return True
    