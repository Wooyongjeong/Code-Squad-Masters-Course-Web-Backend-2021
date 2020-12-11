# 3단계: 루빅스 큐브 구현하기
- [참고 링크](https://cube3x3.com/%ED%81%90%EB%B8%8C%EB%A5%BC-%EB%A7%9E%EC%B6%94%EB%8A%94-%EB%B0%A9/#notation)를 참고해서 루빅스 큐브를 구현한다.
- 큐브는 W, B, G, Y, O, R의 6가지 색깔을 가지고 있다.
- 입력: 각 조작법을 한 줄로 입력받는다.
- 출력: 큐브의 6면을 펼친 상태로 출력한다.
- Q를 입력받으면 프로그램을 종료하고, 조작 받은 명령의 갯수를 출력시킨다.

## 큐브의 초기 상태
```
                B B B  
                B B B
                B B B

 W W W     O O O     G G G     Y Y Y 
 W W W     O O O     G G G     Y Y Y 
 W W W     O O O     G G G     Y Y Y 
 
                R R R 
                R R R 
                R R R 
```

## 프로그램 예시
```
(초기 상태 출력)

CUBE> FRR'U2R

F
(큐브상태)

R
(큐브상태)

...

R
(큐브상태)

CUBE> Q
경과시간: 00:31 //추가 구현 항목
조작갯수: 6
이용해주셔서 감사합니다. 뚜뚜뚜.
```

## 추가 구현 기능
- 프로그램 종료 시 경과 시간 출력
- 큐브의 무작위 섞기 기능
- 모든 면을 맞추면 축하 메시지와 함께 프로그램을 자동 종료

# <br> 구현 내용
## 구현 언어
python 언어를 사용하였습니다.

## 1단계, 2단계에서 구현한 내용 import
```python
from push_word import push_left, push_right
from plane_cube import plane_cube
```
1단계의 단어 밀기 함수와, 2단계의 3x3 평면 큐브 클래스를 import 하였습니다.

## plane_cube 클래스 생성자 수정
```python
class plane_cube:
    def __init__(self, color=None):
        if color is None:
            self.cube = [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']]
        else:
            self.cube = [[color for _ in range(3)] for _ in range(3)]
        self.valid_commands = ["U", "U'", "R", "R'", "L", "L'", "B", "B'", "Q"]
```
- `plane_cube` 클래스의 생성자에 default parameter `color`를 추가하였습니다.
- 생성자를 호출할 때 `color` 문자열을 지정해주었다면, `color` 문자열로 큐브를 초기화합니다.
## cube 클래스 정의
```python
class cube():
    def __init__(self):
        self.start_time = time()
        self.cube = [
            plane_cube('B').cube,
            plane_cube('W').cube, plane_cube('O').cube, plane_cube('G').cube, plane_cube('Y').cube,
            plane_cube('R').cube
        ]
        self.answer = deepcopy(self.cube)
        self.count = 0
        self.print_cube()
        self.valid_commands = ["U", "U'", "L", "L'", "F", "F'", "R", "R'", "B", "B'", "D", "D'", "Q"]
        self.mix_cube()
        self.enter_commands()
```
- `self.start_time`: 추가 구현 기능인 `프로그램 종료 시 경과 시간 출력`을 위해 프로그램 시작 시간을 저장합니다.
- `self.cube`: 루빅스 큐브의 상태를 저장하는 리스트입니다.
    - 수정한 `plane_cube` 객체의 생성자에 큐브의 초기 상태에 맞는 색을 각각 지정하여 초기화합니다.
- `self.answer`: 추가 구현 기능인 `모든 면을 맞추면 축하 메시지와 함께 프로그램을 자동 종료`를 위한 큐브의 정답 큐브 리스트입니다.
    - 위의 `self.cube`를 `copy` 모듈의 `deepcopy`를 이용하여 깊은 복사하여 저장합니다.
- `self.count`: 프로그램 예시의 `조작갯수`를 출력하기 위해 선언하였습니다.
- `self.print_cube()`: 큐브의 현재 상태를 출력하는 함수입니다.
- `self.valid_commands`: 유효한 명령어 리스트입니다.
- `self.mix_cube()`: 추가 구현 기능인 `큐브의 무작위 섞기 기능`을 위해 구현한 함수입니다.
- `self.enter_commands()`: 사용자로부터 입력을 받아 명령어를 처리하는 함수입니다.

이후의 함수들은 모두 cube 클래스의 멤버 함수입니다.
## mix_cube() 함수
```python
def mix_cube(self):
    while True:
        want_random = input('큐브를 무작위로 섞으시겠습니까? (Y/N) > ')
        if want_random == 'Y' or want_random == 'y':
            random_count = randrange(10, 41)
            print(f"{random_count}번 큐브를 섞습니다...")
            random_commands = [choice(self.valid_commands[:-1]) for _ in range(random_count)]
            for command in random_commands:
                self.process_command(command)
            print("큐브 섞기 완료")
            self.print_cube()
            break
        elif want_random == 'N' or want_random == 'n':
            break
        else:
            print('Y 또는 N으로 입력해주세요')
```
1. 사용자로부터 큐브를 무작위로 섞을지 여부를 입력받습니다.
1. `Y`나 `y`를 입력했다면 `random` 모듈을 이용하여 [10, 40] 범위에서 무작위 정수를 뽑습니다.
1. 뽑은 정수만큼 유효한 명령어 리스트인 `self.valid_commands`에서 무작위로 추출하여 명령어를 실행합니다.
    - 이 때, 리스트 뒤에 `[:-1]`를 붙입니다. `self.valid_commands`의 마지막 요소는 프로그램을 종료하는 `Q` 명령어이기 때문입니다.
1. `N`이나 `n`을 입력했다면 큐브를 섞지 않고 반복문을 종료하며 함수를 return합니다.
1. 이외의 문자열을 입력했다면, 다시 입력받습니다.

## print_cube() 함수
```python
def print_cube(self):
    s = ''
    s += self.print_one_cube(True)
    s += '\n'
    for line in range(3):
        s += ' '
        for cube_index in range(1, 5):
            s += self.print_four_cube(cube_index, line)
        s += '\n'
    s += '\n'
    s += self.print_one_cube(is_first=False)
    print(s)
```
1. 큐브의 상태를 출력하는 함수입니다.
1. `self.print_one_cube()`와 `self.print_four_cube()`는 문제의 큐브의 상태를 출력하는 부분처럼 출력하기 위해 호출합니다.
    - 첫 줄에는 `self.cube[0]`의 내용을 출력합니다. (`self.print_one_cube()` 이용)
    - 둘째 줄에는 `self.cube[1]`부터 `self.cube[4]`까지의 내용을 출력합니다. (`self.print_four_cube()` 이용)
    - 마지막 줄에는 `self.cube[-1]`의 내용을 출력합니다. (`self.print_one_cube()` 이용)

## enter_commands() 함수
```python
def enter_commands(self):
    while True:
        cmd = input('CUBE> ')
        if cmd == 'Q':
            self.exit_program()
            break
        command_count = 1
        for i in range(len(cmd)):
            if cmd[i] == "'":
                continue
            command = cmd[i]
            if '1' <= command <= '9':
                command_count = int(command)
                continue
            if i + 1 != len(cmd) and cmd[i+1] == "'":
                command += "'"
            if self.check(command) == True:
                for _ in range(command_count):
                    print(command)
                    self.process_command(command)
                    self.count += 1
                    self.print_cube()
                    self.compare_to_answer()
                command_count = 1
            else:
                print(command)
                print(f"잘못된 입력입니다. 입력은 {self.valid_commands} 만 가능합니다.")
                break
```
1. 반복문을 돌며 사용자로부터 입력을 받습니다. 이 때, 간단한 프롬프트 `CUBE> `를 출력합니다.
1. 사용자가 `Q`를 입력했다면 프로그램을 종료하는 함수 `self.exit_program()`을 호출합니다.
1. 2단계에서 구현한 내용과 동일한 로직으로 `'`을 처리합니다.
1. 3단계에서 추가된 숫자 명령어도 처리하기 위해 `command_count` 변수를 선언하였습니다.
    - 명령어가 숫자라면 `command_count`에 숫자를 저장 후, 다음 반복문을 돌 때 명령어를 `command_count`만큼 반복하여 처리한 후, 1로 초기화합니다.
1. 명령어는 `self.process_command()` 함수를 호출하여 처리합니다.
1. 명령어를 처리할 때마다 클래스의 멤버인 `self.count`를 1만큼 증가합니다.
1. 이후 큐브상태를 출력하고, 명령어를 처리할 때마다 `self.compare_to_answer()` 함수를 호출하여 추가 현 기능인 `모든 면을 맞추면 축하 메시지와 함께 프로그램을 자동 종료`를 구현하였습니다.

## check() 함수
```python
def check(self, command):
    return True if command in self.valid_commands else False
```
사용자가 입력한 명령어가 유효한 명령어인지 판별하는 함수입니다.

## process_command() 함수
```python
def process_command(self, command):
    if command == "U":
        self.up()
    elif command == "U'":
        self.up(clockwise=False)

    ... (중략)

    elif command == "D":
        self.down()
    elif command == "D'":
        self.down(clockwise=False)
```
1. 인자 `parameter`로 들어온 명령어에 따라 큐브를 돌리는 함수입니다.
1. 각 명령어에 대응되는 `self.up()`, `self.left()`, `self.front()`, `self.right()`, `self.back()`, `self.down()`을 호출합니다.
    - 이 때, 예를 들어 큐브의 윗쪽 부분을 시계 반대방향으로 돌리는 `U'` 명령어의 경우에는 `clockwise` 인자를 `False`로 지정하여 시계 반대방향임을 명시하여 `self.up()` 함수를 호출합니다.

## rotate_clockwise(), rotate_counterclockwise() 함수
```python
def rotate_clockwise(self, m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def rotate_counterclockwise(self, m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]
    return ret
```
1. 각각 2차원 배열(3x3 큐브)을 시계 방향, 시계 반대방향으로 회전하여 return해주는 함수입니다.
1. [출처](https://deepwelloper.tistory.com/117)를 참조하였습니다.

## 큐브를 돌리는 up(), left(), ... , down() 함수
```python
def left(self, clockwise=True):
    cube_string = ''
    rotating_planes = [0, 2, 5, 4]
    for cube_index in rotating_planes:
        c = self.cube[cube_index]
        for i in range(3):
            cube_string += c[i][0]
    if clockwise == True:
        self.cube[1] = self.rotate_clockwise(self.cube[1])
        cube_string = push_right(3, cube_string)
    else:
        self.cube[1] = self.rotate_counterclockwise(self.cube[1])
        cube_string = push_left(3, cube_string)
    index = 0
    for cube_index in rotating_planes:
        c = self.cube[cube_index]
        for i in range(3):
            c[i][0] = cube_string[index]
            index += 1
```
up(), left(), ... , down() 함수 모두 비슷한 로직이므로 left() 함수만 설명하겠습니다.
1. 1단계에서 구현한 `push_left()`, `push_right()`를 이용하였습니다. 이 함수들의 인자는 문자열이므로 `cube_string`을 선언하였습니다.
1. `self.cube[0]`을 윗면, `self.cube[1] ~ self.cube[4]`를 옆면, `self.cube[-1]`를 아랫면이라고 가정하고 로직을 작성하였습니다.
1. 큐브를 바라보고 있는 방향은 `self.cube[2]`를 기준으로 하였습니다. `self.cube[2]`가 보이도록 잡고 큐브를 돌리도록 로직을 작성하였습니다.
1. 회전하는 방향에 따라 회전하는 면들의 리스트인 `rotating_planes`를 각 함수에서 다르게 지정해주었습니다.
1. `left()`는 `self.cube[2]`를 눈앞에 놓고 왼쪽을 돌리는 것입니다. 다른 함수들도 마찬가지입니다.
1. 이 때 회전해야하는 큐브는 `self.cube[0]`, `self.cube[2]`, `self.cube[5]`, `self.cube[4]`입니다.
1. 따라서 `rotating_planes`는 `[0, 2, 5, 4]`가 됩니다.
    - 왼쪽으로 회전할 때 돌아가는 부분을 for문을 돌며 `cube_string` 문자열에 `rotating_planes` 리스트 순서대로 저장합니다.
    - 큐브를 잡고 돌리면 한쪽 면은 돌리는 방향으로 회전하므로, `left()`의 default parameter인 `clockwise` 변수에 따라 `self.rotate_clockwise`나 `self.rotate_counterclockwise`를 호출합니다.
        - `left()`에서는 회전하는 면은 `self.cube[1]`이므로 `self.cube[1]` 면을 회전해줍니다.
    - 시계 방향으로 돌리는 것은 `push_right()`을 호출하는 것과 같은 결과입니다. 이 때, 3만큼 오른쪽으로 밀어냅니다. 반대 방향은 `push_left()`를 호출합니다.
1. `push_left()`나 `push_right()` 함수를 통해 얻은 결과를 이용하여 현재 큐브 상태를 갱신합니다. `cube_string`에 저장된 순서대로, `rotating_planes` 리스트의 순서대로 각 면을 업데이트 합니다.


## compare_to_answer() 함수
```python
def compare_to_answer(self):
    if self.cube == self.answer:
        self.exit_program(is_answer=True)
```
1. `self.cube`와 `self.answer`을 비교하여 같다면 프로그램을 종료하는 함수인 `self.exit_program()`을 호출합니다.
1. 이 때 인자로 `is_answer`을 `True`로 지정해주며 호출합니다.

## exit_program() 함수
```python
def exit_program(self, is_answer=False):
    end_time = time()
    elapsed_time = int(end_time - self.start_time)
    print(f"경과 시간: {elapsed_time // 60:02d}:{elapsed_time % 60:02d}")
    print(f"조작갯수: {self.count}")
    if is_answer == True:
        print("축하합니다! 모든 면을 맞추셨습니다.")
    print("이용해주셔서 감사합니다. 뚜뚜뚜.")
    exit(0)
```
1. 추가 구현기능인 `프로그램 종료 시 경과 시간 출력`을 구현하기 위해 `end_time`을 `time` 모듈을 이용하여 선언하였습니다.
    - `end_time`에서 `self.start_time`을 빼기 연산을 통해 경과 시간을 계산합니다.
    - 이후 경과 시간을 화면에 출력합니다.
1. 문제의 프로그램 예시처럼 `조작갯수`를 출력합니다. 클래스 멤버 `self.count`를 이용하였습니다.
1. 인자로 들어온 `is_answer`은 default parameter로, `True`라면 정답을 맞추어 종료되는 경우, `False`라면 사용자가 명령어 `Q`를 통해 종료하는 경우를 나누어 구현하였습니다.
    - 이를 통해 추가 구현기능인 `모든 면을 맞추면 축하 메시지와 함께 프로그램을 자동 종료`를 구현하였습니다.
    - `is_answer`가 `True`라면 축하 메시지를 출력합니다.
1. 이후 `sys` 모듈의 `exit()` 함수를 이용하여 프로그램을 종료합니다.

## 클래스 생성자 호출
```python
cube()
```
클래스 생성자를 호출하여 구현한 내용을 동작하게 합니다.