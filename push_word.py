# 왼쪽으로 밀기
def push_left(num, word):
    if num > 0:
        num %= len(word)
        return word[num:] + word[:num]
    else:
        return push_right(-num, word)
        
# 오른쪽으로 밀기
def push_right(num, word):
    if num > 0:
        num %= len(word)
        return word[len(word)-num:] + word[:len(word)-num]
    else:
        return push_left(-num, word)
