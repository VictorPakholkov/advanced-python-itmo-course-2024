import sys
sys.path.insert(0, '/home/avigdor/projects/advanced_python_itmo_course/hw_3/matrix_operations_pakholkov_package/src')

from matrix_operations import NMatrix
import numpy as np

np.random.seed(0)
matrix1 = np.random.randint(0, 10, (10, 10))
matrix2 = np.random.randint(0, 10, (10, 10))

matrix1 = NMatrix(matrix1)
matrix2 = NMatrix(matrix2)

add_res = str(matrix1 + matrix2)
matr_mult_res = str(matrix1 * matrix2)
pair_mult_res = str(matrix1 @ matrix2)

with open('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.1/matrix@.txt', 'w') as file:
    file.write(pair_mult_res)

with open('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.1/matrix*.txt', 'w') as file:
    file.write(matr_mult_res)

with open('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.1/matrix+.txt', 'w') as file:
    file.write(add_res)

