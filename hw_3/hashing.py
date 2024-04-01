import sys
sys.path.insert(0, '/home/avigdor/projects/advanced_python_itmo_course/hw_3/matrix_operations_pakholkov_package/src')

from matrix_operations import NMatrixE
import numpy as np

A = NMatrixE(np.array([[1, 2], [3, 4]]))
C = NMatrixE(np.array([[5, 6], [7, 8]]))

B = NMatrixE(np.array([[2, 3], [4, 5]]))
D = B

A.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.3/A.txt')
B.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.3/B.txt')
C.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.3/C.txt')
D.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.3/D.txt')

if hash(A) == hash(C) and A != C and B == D:
    print("Hash collision detected!")

AB = NMatrixE(A@B)
CD = NMatrixE(C@D)

AB.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.3/AB.txt')
CD.to_file('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.3/CD.txt')


hash1 = hash(AB)
hash2 = hash(CD)


with open('/home/avigdor/projects/advanced_python_itmo_course/hw_3/artifacts/3.3/hash.txt', 'w') as file:
    file.write(f'AB hash: {hash1} \n CD hash: {hash2}')