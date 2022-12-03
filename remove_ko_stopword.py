from konlpy.tag import Okt

okt = Okt()

example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"

stop_words = set(stop_words.split(' '))  # 공백을 기준으로 불용어를 나눈다.
word_tokens = okt.morphs(example)  # 형태소들을 가져온다.

# 형태소들 중, 불용어가 아닌 형태소를 가져온다.
result = [word for word in word_tokens if not word in stop_words]

print('불용어 제거 전 :', word_tokens)
print('불용어 제거 후 :', result)

# 불용어 제거 전 : ['고기', '를', '아무렇게나', '구', '우려', '고', '하면', '안', '돼', '.', '고기', '라고', '다', '같은', '게', '아니거든', '.', '예컨대', '삼겹살, '.']
# 불용어 제거 후 : ['고기', '하면', '.', '고기', '라고', '다', '아니거든', '.', '예컨대', '삼겹살', '을', '중요한', '있지', '.']
