import numpy as np

Array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

ele1 = Array1[0][0] * Array1[0][0]
ele2 = Array1[1][1] * Array1[1][1]
ele3 = Array1[2][2] * Array1[2][2]

print(ele1, ele2, ele3)

newArray = np.array([ele1, ele2, ele3])
print(newArray)