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

# 데이터가 섞이지 않은 채 어느 지점에서 데이터를 앞과 뒤로 분리한다.
num_of_train = int(len(X) * 0.8)  # 데이터의 전체 길이의 80%에 해당하는 길이값을 구한다.
num_of_test = int(len(X) - num_of_train)  # 전체 길이에서 80%에 해당하는 길이를 뺀다.
print('훈련 데이터의 크기 :', num_of_train)
print('테스트 데이터의 크기 :', num_of_test)

X_test = X[num_of_train:]  # 전체 데이터 중에서 20%만큼 뒤의 데이터 저장
y_test = y[num_of_train:]  # 전체 데이터 중에서 20%만큼 뒤의 데이터 저장
X_train = X[:num_of_train]  # 전체 데이터 중에서 80%만큼 앞의 데이터 저장
y_train = y[:num_of_train]  # 전체 데이터 중에서 80%만큼 앞의 데이터 저장

print('X 테스트 데이터 :')
print(X_test)
print('y 테스트 데이터 :')
print(list(y_test))

"""
훈련 데이터의 크기 : 4
테스트 데이터의 크기 : 1
X 테스트 데이터 :
[[20 21 22 23]]
y 테스트 데이터 :
[24]
"""
