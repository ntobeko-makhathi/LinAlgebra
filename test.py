import Matrix

m = Matrix.Matrix.matrix([[1, 2], [3, 4]])
m.display("Determinant")

m2 = Matrix.Matrix.matrix([[5, 6], [7, 8]])
m2.display("adjoint")

m3 = Matrix.Matrix.matrix(m.add(m2))
m3.display("determinant")

m4 = Matrix.Matrix.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m4.display("rank")

m5 = Matrix.Matrix.matrix([[1, 2], [3, 4], [5, 6]])
m5.display("determinant")

m6 = Matrix.Matrix.matrix([[1, 2], [3, 4]])
m6.display("inverse")

m7 = Matrix.Matrix.matrix([[1, 2], [3, 4]])
m7.display("transpose") 
