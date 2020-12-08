# <br>1단계: 단어 밀어내기 구현하기
1. 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
1. 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
1. 밀려나간 단어는 반대쪽으로 채워진다.

# <br>구현 내용
## 구현 언어
python 언어를 사용하였습니다.
## push_left() 함수
``` python
def push_left(num, word):
    if num > 0:
        num %= len(word)
        return word[num:] + word[:num]
    else:
        return push_right(-num, word)
```
1. 우선 사용자가 입력한 정수 숫자가 0보다 작다면 반대 방향(오른쪽)으로 밀어야 하기 때문에 입력한 숫자의 음수를 push_right()에 인자로 넣어 호출하였습니다.
1. 사용자가 입력한 정수 숫자를 단어의 길이와 나머지 연산처리 해줍니다.
1. 만약 단어의 길이가 5라면, 3번 왼쪽으로 밀어내는 것과 8번 왼쪽으로 밀어내는 것의 결과는 같기 때문입니다.
1. 왼쪽으로 밀어내는 것이기 때문에 밀어낼 숫자만큼의 위치부터 단어 끝까지 슬라이스한 부분 `word[num:]`에 단어의 처음부터 밀어낼 숫자 전까지 슬라이스한 부분 `word[:num]`을 붙여 return합니다.

## push_right() 함수
```python
def push_right(num, word):
    if num > 0:
        num %= len(word)
        return word[len(word)-num:] + word[:len(word)-num]
    else:
        return push_left(-num, word)
```
1. push_left()와 마찬가지로 사용자가 입력한 정수 숫자가 0보다 작다면 반대 방향(왼쪽)으로 밀어야 하므로 입력한 숫자의 음수를 push_left()에 인자로 넣어 호출합니다.
1. 마찬가지로 입력한 정수 숫자를 단어의 길이와 나머지 연산처리 해줍니다.
1. 이번에는 오른쪽으로 밀어내야 하기 때문에, 전체 길이에서 밀어낼 숫자만큼 뺀만큼의 위치부터 단어 끝까지 슬라이스한 부분 `word[len(word)-num:]`에 단어의 처음부터 해당 위치 전까지 슬라이스한 부분 `word[:len(word)-num]`을 붙여 return합니다.

## 입력
```python
word, num, direction = input('> ').split()
while int(num) < -100 or int(num) >= 100:
    num = int(input('숫자는 -100보다 크거나 같고, 100보다 작아야합니다 > '))
directions = ['L', 'R', 'l', 'r']
while direction not in directions:
    direction = input('방향은 L, R, l, r 중 하나여야 합니다 > ')
```
1. 사용자로부터 `단어` 하나, `정수 숫자` 하나, `L 또는 R(l 또는 r)`을 입력받습니다.
1. 입력한 정수가 -100보다 작거나, 100보다 크거나 같다면 잘못 입력한 것이므로 다시 입력받습니다.
1. 방향 역시 `L, R, l, r` 중 하나가 아니라면 잘못 입력한 것이므로 다시 입력받습니다.

## 출력
```python
if direction == 'L' or direction == 'l':
    answer = push_left(int(num), word)
    print(answer)
elif direction == 'R' or direction == 'r':
    answer = push_right(int(num), word)
    print(answer)
```
1. 밀어낼 방향이 왼쪽이면 push_left() 함수를 호출하여 결과를 출력합니다.
1. 오른쪽이라면 push_right() 함수를 호출하여 결과를 출력합니다.