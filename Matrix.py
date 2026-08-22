class Matrix:
    def __init__(self):
        self.matrix = self.create()
        self.rows = self.matrix.lenght()
        self.columns =self.matrix[0].lenght()

    def __init__(self, matrix):
            #This constructor takes predefined 
            self.matrix = matrix
            self.rows = self.matrix.lenght()
            self.columns =self.matrix[0].lenght()
    def det(self, m):
        d=0
        if len(m)<1:
            return
        if len(self.m)==1:
            return m[0][0]
        else:
            for j in range(len(m[0])):
                minor=[]
                for i in range(1,len(m[0])):
                    minor.append((m[i][:j]+m[i][j+1:]))
        
                d+=m[0][j]*((-1)**(j))*self.det(minor)
                
            return d
    def create(self):
        matrix =[]
        row = int(input("How many rows is the matrix:\n"))
        column = int(input("How many column is the matrix:\n"))

        for i in range(row):
            row_value = []
            print(f"Enter Row {i+1} values one by one:")
            for j in range(column):
                a = int(input(""))
                row_value.append(a)
            matrix.append(row_value)
        return matrix

    def display(self):
        print("\nmatrix A:\n")
        for rw in self.matrix:
            print(rw)    
        print (f"\ndet(A)={self.det(self.matrix)}")

    def add(self, otherMatrix):
        result=[]
        if (self.rows==otherMatrix.rows and self.columns==otherMatrix.colums):
            for i in range(self.rows):
                row=[]
                for j in range(self.columns):
                    row.append(self.matrix[i][j]+otherMatrix.matrix[i][j])
                result.append(row)
            return result
        else:
            return "illegal operation"

