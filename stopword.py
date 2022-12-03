import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')

stop_words_list = stopwords.words('english')
print('불용어 개수 :', len(stop_words_list))
print('불용어 10개 출력 :', stop_words_list[:10])

# 불용어 개수 : 179
# 불용어 10개 출력 : ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"]
