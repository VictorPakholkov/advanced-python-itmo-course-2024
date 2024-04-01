import sys
sys.path.insert(0, '/home/avigdor/projects/advanced_python_itmo_course/hw_3/matrix_operations_pakholkov_package/src')

from matrix_operations import NMatrixE
import numpy as np

np.random.seed(0)
matrix1 = np.random.randint(0, 10, (10, 10))
matrix2 = np.random.randint(0, 10, (10, 10))

matrix1e = NMatrixE(matrix1)
matrix2e = NMatrixE(matrix2)


add_res = matrix1e + matrix2e
add_res = NMatrixE(add_res)
matr_mult_res = matrix1e * matrix2e
matr_mult_res = NMatrixE(matr_mult_res)
pair_mult_res = matrix1e @ matrix2e
pair_mult_res = NMatrixE(pair_mult_res)



add_res.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.2/matrix+.txt')
matr_mult_res.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.2/matrix*.txt')
pair_mult_res.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.2/matrix@.txt')