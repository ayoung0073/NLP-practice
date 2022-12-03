from konlpy.tag import Okt
from konlpy.tag import Kkma

okt = Okt()
kkma = Kkma()

input = "열심히 NLP 공부하고, 연말에는 유럽 여행 가자!"
print("input :", input)

# Okt(Open Korea Text) 형태소 분석기
print('OKT 형태소 분석 :', okt.morphs(input))
print('OKT 품사 태깅 :', okt.pos(input))
print('OKT 명사 추출 :', okt.nouns(input))

# OKT 형태소 분석 : ['열심히', 'NLP', '공부', '하고', ',', '연말', '에는', '유럽', '여행', '가자', '!']
# OKT 품사 태깅 : [('열심히', 'Adverb'), ('NLP', 'Alpha'), ('공부', 'Noun'), ('하고', 'Josa'), (',', 'Punctuation'), ('연말', 'Noun'), ('에는', 'Josa'), ('유럽', 'oun'), ('가자', 'Verb'), ('!', 'Punctuation')]
# OKT 명사 추출 : ['공부', '연말', '유럽', '여행']

print('---------------------------------------------------------------------------------------------')

# 꼬꼬마(Kkma) 형태소 분석기
print('꼬꼬마 형태소 분석 :', kkma.morphs(input))
print('꼬꼬마 품사 태깅 :', kkma.pos(input))
print('꼬꼬마 명사 추출 :', kkma.nouns(input))

# 꼬꼬마 형태소 분석 : ['열심히', 'NLP', '공부', '하', '고', ',', '연말', '에', '는', '유럽', '여행', '가자', '!']
# 꼬꼬마 품사 태깅 : [('열심히', 'MAG'), ('NLP', 'OL'), ('공부', 'NNG'), ('하', 'XSV'), ('고', 'ECE'), (',', 'SP'), ('연말', 'NNG'), ('에', 'JKM'), ('는', 'JX'), (', 'NNG'), ('가자', 'NNG'), ('!', 'SF')]
# 꼬꼬마 명사 추출 : ['공부', '연말', '유럽', '여행', '가자']
