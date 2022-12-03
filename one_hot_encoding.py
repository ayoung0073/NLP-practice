from konlpy.tag import Okt

# 토큰화
okt = Okt()  # okt(open korea text) 형태소 분석기
tokens = okt.morphs("나는 자연어 처리를 배운다")  # 토큰화 진행
print(tokens)
### ['나', '는', '자연어', '처리', '를', '배운다']

# 각 토큰에 대해 고유한 정수 부여
# (지금은 고려하지 않았지만) 빈도수 순으로 단어를 정렬하여 정수를 부여하는 경우가 많음
# (NLTK의 FreqDist/keras의 전처리 도구 토크나이저/Counter의 most_common() 함수을 이용할 수 있다.)
word_to_index = {word: index for index, word in enumerate(tokens)}
print('단어 집합 :', word_to_index)
### 단어 집합 : {'나': 0, '는': 1, '자연어': 2, '처리': 3, '를': 4, '배운다': 5}

# 원-핫 벡터를 만들어내는 함수
def one_hot_encoding(word, word_to_index):
    one_hot_vector = [0]*(len(word_to_index))
    index = word_to_index[word]
    one_hot_vector[index] = 1
    return one_hot_vector

one_hot_vector = one_hot_encoding("처리", word_to_index)
print(one_hot_vector)
### [0, 0, 0, 1, 0, 0] -> 원-핫 벡터

