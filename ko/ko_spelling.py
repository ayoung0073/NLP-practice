from hanspell import spell_checker

sentence = "나는 정말 맟춤법 틀리는 사람 이해가 안되 외 그러는 거야 잘 쓰면돼지 "
spelled_sentence = spell_checker.check(sentence)

hanspell_sentence = spelled_sentence.checked
print(hanspell_sentence)
"""
나는 정말 맞춤법 틀리는 사람 이해가 안 돼 외 그러는 거야 잘 쓰면 되지
"""