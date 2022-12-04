from sklearn.model_selection import train_test_split
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

# train_size와 test_size는 줄 중 하나만 기재해도 된다. (값이 1보다 작으면 비율을 나타낸다.)
# train : test = 7 : 3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=1234)
print('X 훈련 데이터 :')
print(X_train)
print('X 테스트 데이터 :')
print(X_test)

print('y 훈련 데이터 :')
print(y_train)
print('y 테스트 데이터 :')
print(y_test)

"""
X 훈련 데이터 :
[[ 5  6  7  8]
 [10 11 12 13]
 [15 16 17 18]]
X 테스트 데이터 :
[[20 21 22 23]
 [ 0  1  2  3]]
y 훈련 데이터 :
[ 9 14 19]
y 테스트 데이터 :
[24  4]
"""