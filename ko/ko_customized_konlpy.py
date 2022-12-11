from ckonlpy.tag import Twitter

twitter = Twitter()
twitter.add_dictionary('은경이', 'Noun')
print(twitter.morphs('은경이는 회사에 있습니다.')) # 형태소 출력
"""
['은경이', '는', '회사', '에', '있습니다', '.']
"""