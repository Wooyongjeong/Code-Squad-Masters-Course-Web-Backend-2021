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
while -100 <= int(num) < 100:
    print('숫자는 -100보다 크거나 같고, 100보다 작아야합니다 >')
    num = int(input())
while direction != 'L' or direction != 'R' or direction != 'l' or direction != 'r':
    print('방향은 L, R, l, r 중 하나여야 합니다 >')
    direction = input()
if direction == 'L' or direction == 'l':
    answer = push_left(int(num), word)
    print(answer)
elif direction == 'R' or direction == 'r':
    answer = push_right(int(num), word)
    print(answer)