# 리스트의 리스트 또는 행렬 또는 뒤에서 배울 개념인 2D 텐서
sequences = [['a', 1], ['b', 2], ['c', 3]]
X, y = zip(*sequences)
print('X 데이터:', X)
print('y 데이터:', y)

"""
X 데이터 : ('a', 'b', 'c')
y 데이터: (1, 2, 3)
"""