from pykospacing import Spacing

# sent: 간격
sentence = "안녕하세요제이름은문아영입니다이거띄어쓰기얼마나될까정말궁금하네요"
spacing = Spacing()
kospacing_sentence = spacing(sentence)

print(sentence)
print(kospacing_sentence)