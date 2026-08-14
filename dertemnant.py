class Matrix:
    def __init__(self):
        self.matrix = self.create()

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
        

