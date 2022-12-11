from konlpy.tag import Okt

# 기존 형태소 분석기 문제
tokenizer = Okt()
print(tokenizer.morphs('에이비식스 이대휘 최애돌 기부 요정 어쩔티비'))
"""
['에이', '비식스', '이대', '휘', '최애', '돌', '기부', '요정', '어쩔', '티비']
"""