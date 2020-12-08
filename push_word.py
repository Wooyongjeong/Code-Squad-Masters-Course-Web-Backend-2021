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

# 입력 받기
word, num, direction = input('> ').split()
while int(num) < -100 or int(num) >= 100:
    num = int(input('숫자는 -100보다 크거나 같고, 100보다 작아야합니다 > '))
directions = ['L', 'R', 'l', 'r']
while direction not in directions:
    direction = input('방향은 L, R, l, r 중 하나여야 합니다 > ')

# 출력하기
if direction == 'L' or direction == 'l':
    answer = push_left(int(num), word)
    print(answer)
elif direction == 'R' or direction == 'r':
    answer = push_right(int(num), word)
    print(answer)