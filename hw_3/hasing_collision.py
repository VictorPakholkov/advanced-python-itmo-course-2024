import sys
sys.path.insert(0, '/home/avigdor/projects/advanced_python_itmo_course/hw_3/matrix_operations_pakholkov_package/src')

from matrix_operations import NMatrixE
import numpy as np

# Obviously, for collision to be detected, we need to hash matricies, elements of which add up to the same number 

a = NMatrixE([[1, 2], [3, 4]])
b = NMatrixE([[2, 2], [2, 4]])

if hash(a) == hash(b):
    print("Hash collision detected!")