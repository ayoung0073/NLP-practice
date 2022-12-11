import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('movies_metadata.csv', low_memory=False)
# print(data.head(2)) # 데이터 형식을 보기 위해 상위 2개의 샘플을 출력해본다.
data = data.head(20000)  # 데이터의 양을 줄여서 학습을 진행
# title(제목), overview(줄거리) 필드만 사용할 것이다.

### TF-IDF를 연산할 때 데이터에 Null 값이 들어있으면 에러가 발생.
# 선행 작업: TF-IDF의 대상이 되는 data의 overview 열에 결측값에 해당하는 Null 값이 있는지 확인한 후, Null 값을 빈값(empty value)으로 대체한다.
print('overview 열의 결측값의 수:', data['overview'].isnull().sum())
data['overview'] = data['overview'].fillna('')  # 결측값이 있던 행에 특정값으로 채워넣는 pandas의 fillna()

### overview열에 대해서 TF-IDF 행렬을 구한 후 행렬의 크기를 출력한다.
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])
print('TF-IDF 행렬의 크기(shape) :', tfidf_matrix.shape)
"""
TF-IDF 행렬의 크기(shape) : (20000, 47487) -> 20000행, 47487열
20,000개의 영화를 표현하기 위해서 총 47,487개의 단어가 사용되었음을 의미한다.
"""
### 코사인의 유사도를 구한다.
cosine_similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
print('코사인 유사도 연산 결과 :', cosine_similarity.shape)
"""
코사인 유사도 연산 결과 : (20000, 20000)
"""
# 20,000개의 각 문서 벡터(영화 줄거리 벡터)와 자기 자신을 포함한 20,000개의 문서 벡터 간의 유사도가 기록된 행렬이다.

### 기존 데이터프레임으로부터 영화의 타이틀을 key, 영화의 인덱스를 value로 하는 딕셔너리 title_to_index를 만들어둔다.
title_to_index = dict(zip(data['title'], data.index))


### 선택한 영화의 제목을 입력하면 코사인 유사도를 통해 가장 overview가 유사한 n개의 영화를 찾아내는 함수 정의
def get_recommendations(title, size, cosine_similarity=cosine_similarity):
    # 선택한 영화의 타이틀로부터 해당 영화의 인덱스를 받아온다.
    index = title_to_index[title]

    # 해당 영화와 모든 영화와의 유사도를 가져온다.
    similarity_scores = list(enumerate(cosine_similarity[index]))

    # 유사도에 따라 영화들을 정렬한다.
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 영화를 받아온다.
    similarity_scores = similarity_scores[1:size + 1]

    # 가장 유사한 10개의 영화의 인덱스를 얻는다.
    movie_indices = [idx[0] for idx in similarity_scores]

    # 가장 유사한 10개의 영화의 제목을 리턴한다.
    return data['title'].iloc[movie_indices]


print(get_recommendations('The Dark Knight Rises', size=6))
"""
12481                       The Dark Knight
150                          Batman Forever
1328                         Batman Returns
15511            Batman: Under the Red Hood
585                                  Batman
9230     Batman Beyond: Return of the Joker
"""
