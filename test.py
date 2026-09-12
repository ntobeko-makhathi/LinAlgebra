import Matrix

m = Matrix.Matrix.matrix([[1, 2], [3, 4]])
m.display()

m2 = Matrix.Matrix.matrix([[5, 6], [7, 8]])
m2.display()

m3 = Matrix.Matrix.matrix(m.add(m2))
m3.display()

m4 = Matrix.Matrix.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m4.display()

m5 = Matrix.Matrix.matrix([[1, 2], [3, 4], [5, 6]])
m5.display()
