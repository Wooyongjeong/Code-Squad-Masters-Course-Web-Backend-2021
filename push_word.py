def push_left(num, word):
    if num > 0:
        num %= len(word)
        return word[num:] + word[:num]
    else:
        return push_right(-num, word)
        
def push_right(num, word):
    if num > 0:
        num %= len(word)
        return word[len(word)-num:] + word[:len(word)-num]
    else:
        return push_left(-num, word)

word, num, direction = input('> ').split()
if direction == 'L' or direction == 'l':
    answer = push_left(int(num), word)
    print(answer)
elif direction == 'R' or direction == 'r':
    answer = push_right(int(num), word)
    print(answer)