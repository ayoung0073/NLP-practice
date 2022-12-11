doc1 = "apple banana everyone like likey watch card holder"
doc2 = "apple banana coupon passport love you"

# 토큰화
tokenized_doc1 = doc1.split()
tokenized_doc2 = doc2.split()

print('문서1 :', tokenized_doc1)
print('문서2 :', tokenized_doc2)
"""
문서1 : ['apple', 'banana', 'everyone', 'like', 'likey', 'watch', 'card', 'holder']
문서2 : ['apple', 'banana', 'coupon', 'passport', 'love', 'you']
"""

# 합집합
union = set(tokenized_doc1).union(set(tokenized_doc2))
print('문서1과 문서2의 합집합 :', union)

# 교집합
intersection = set(tokenized_doc1).intersection(set(tokenized_doc2))
print('문서1과 문서2의 교집합 :', intersection)
"""
문서1과 문서2의 합집합 : {'passport', 'card', 'watch', 'like', 'coupon', 'you', 'apple', 'banana', 'love', 'everyone', 'holder', 'likey'}
문서1과 문서2의 교집합 : {'apple', 'banana'}
"""

# 자카드 유사도
print('자카드 유사도 :', len(intersection) / len(union))
"""
자카드 유사도 : 0.16666666666666666
"""