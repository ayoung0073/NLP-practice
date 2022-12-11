import numpy as np
from numpy import dot # 벡터 내적, 행렬곱 함수
from numpy.linalg import norm # 벡터 정규화하는 함수

def cos_similarity(A, B):
    return dot(A, B) / (norm(A) * norm(B))

"""
문서1 : 저는 사과 좋아요
문서2 : 저는 바나나 좋아요
문서3 : 저는 바나나 좋아요 저는 바나나 좋아요
"""
doc1 = np.array([0, 1, 1, 1])
doc2 = np.array([1, 0, 1, 1])
doc3 = np.array([2, 0, 2, 2])

print('문서 1과 문서2의 유사도 :', cos_similarity(doc1, doc2))
print('문서 1과 문서3의 유사도 :', cos_similarity(doc1, doc3))
print('문서 2와 문서3의 유사도 :', cos_similarity(doc2, doc3))
"""
문서 1과 문서2의 유사도 : 0.6666666666666667
문서 1과 문서3의 유사도 : 0.6666666666666667
문서 2와 문서3의 유사도 : 1.0000000000000002

문서 1, 문서 2의 코사인 유사도가 같다.
문서 2, 문서 3의 코사인 유사도가 1로 나왔다 -> 유사도의 값이 최대
"""