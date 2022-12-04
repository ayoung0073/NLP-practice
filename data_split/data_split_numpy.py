import numpy as np

np_array = np.arange(0, 25).reshape((5, 5))
print('전체 데이터 :')
print(np_array)

"""
전체 데이터 :
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
"""

X = np_array[:, :4]
y = np_array[:, 4]

print('X 데이터 :')
print(X)
print('y 데이터 :', y)

"""
X 데이터 :
[[ 0  1  2  3]
 [ 5  6  7  8]
 [10 11 12 13]
 [15 16 17 18]
 [20 21 22 23]]
y 데이터 : [ 4  9 14 19 24]
"""