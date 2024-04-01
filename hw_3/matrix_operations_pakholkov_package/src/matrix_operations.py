import numpy as np
import functools

class NMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        if isinstance(matrix, list):
            self.rows = len(matrix)
            self.cols = len(matrix[0]) if matrix else 0
        elif isinstance(matrix, np.ndarray):
            self.rows = matrix.shape[0]
            self.cols = matrix.shape[1]
        else:
            raise ValueError("Matrix must be a 2D list or 2D NumPy array.")

    def __add__(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices have incompatible dimensions for addition.")
        return NMatrix([[a + b for a, b in zip(row, other_row)] for row, other_row in zip(self.matrix, other_matrix.matrix)])

    def __mul__(self, other_matrix):
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            raise ValueError("Matrices have incompatible dimensions for component-wise multiplication.")
        return NMatrix([[a * b for a, b in zip(row, other_row)] for row, other_row in zip(self.matrix, other_matrix.matrix)])

    def __matmul__(self, other_matrix):
        if self.cols != other_matrix.rows:
            raise ValueError("Matrices have incompatible dimensions for matrix multiplication.")
        return NMatrix([[sum(a * b for a, b in zip(row, col)) for col in zip(*other_matrix.matrix)] for row in self.matrix])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


class NMatrixE(np.lib.mixins.NDArrayOperatorsMixin):

    def __init__(self, matrix):
        self._matrix = np.array(matrix)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = np.array(matrix)

    def __len__(self):
        return self.matrix.shape[0]

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        return str(self.matrix)

    def to_file(self, filename):
        np.savetxt(filename, self.matrix)

    def __hash__(self):
        # Simplest hash function possible: sum up all elements in the matrix; ofc it will cause sufficient number of collisions, but this is for demonstration only
        return hash(self.matrix.sum())
    
    @staticmethod
    def matrix_product_memoize(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(a, b):
            key = (hash(a), hash(b))
            if key not in cache:
                cache[key] = func(a, b)
            return cache[key]

        return wrapper

    @matrix_product_memoize
    def matrix_product(self, other):
        return self.__class__(self.matrix @ other.matrix)

