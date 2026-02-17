import numpy as np

matrix1 = np.array([[1,2,3],
                   [3,2,1],
                   [4,2,2]])

matrix2 = np.array([[7,2,1],
                   [5,9,8],
                   [1,7,5]])
# add them
def addMatrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

# use dot product
def dotMatrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)
    
# use cross product
def crossMatrices(matrix1, matrix2):
    return np.cross(matrix1, matrix2)


print(addMatrices(matrix1, matrix2))
print(dotMatrices(matrix1, matrix2))
print(crossMatrices(matrix1, matrix2))