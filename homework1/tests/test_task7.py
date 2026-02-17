from src.task7 import matrix1, matrix2, addMatrices, dotMatrices, crossMatrices
import numpy as np

# check that the output is a matrix, 3 x 3 matrix and it matches the manual output
def test_addMatrices():
    result = addMatrices(matrix1, matrix2)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 3)
    expectedAns = np.array([[ 8,  4,  4],
                              [ 8, 11,  9],
                              [ 5,  9,  7]])
    np.testing.assert_array_equal(result, expectedAns)

# check that the output is a matrix, 3 x 3 matrix and it matches the manual output
def test_dotMatrices():
    result = dotMatrices(matrix1, matrix2)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 3)
    expectedAns = np.array([[ 20,  41,  32],
                              [ 32, 31,  24],
                              [ 40,  40,  30]])
    np.testing.assert_array_equal(result, expectedAns)

# check that the output is a matrix, 3 x 3 matrix and it matches the manual output
def test_crossMatrices():
    result = crossMatrices(matrix1, matrix2)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 3)

    expectedAns = np.array([[ -4,  20,  -12],
                              [ 7, -19,  17],
                              [ -4,  -18,  26]])
    np.testing.assert_array_equal(result, expectedAns)

