def push_left(num, word):
    if num > 0:
        word = list(word)
        num %= len(word)
        return ''.join(word[num:] + word[:num])
    else:
        return push_right(-num, word)
        
def push_right(num, word):
    if num > 0:
        word = list(word)
        num %= len(word)
        return ''.join(word[len(word)-num:] + word[:len(word)-num])
    else:
        return push_left(-num, word)

word, num, direction = input('> ').split()
