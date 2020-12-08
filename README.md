# 2단계: 평면 큐브 구현하기
3 X 3의 2차원 배열이 아래처럼 있다.
```
R R W
G C W
G B B
```

사용자 입력을 받아서 아래의 동작을 하는 프로그램을 구현하시오
```
> U  가장 윗줄을 왼쪽으로 한 칸 밀기 RRW -> RWR
> U' 가장 윗줄을 오른쪽으로 한 칸 밀기 RRW -> WRR
> R  가장 오른쪽 줄을 위로 한 칸 밀기 WWB -> WBW
> R' 가장 오른쪽 줄을 아래로 한 칸 밀기 WWB -> BWW
> L  가장 왼쪽 줄을 아래로 한 칸 밀기 RGG -> GRG (L의 경우 R과 방향이 반대임을 주의한다.)
> L' 가장 왼쪽 줄을 위로 한 칸 밀기 RGG -> GGR
> B  가장 아랫줄을 오른쪽으로 한 칸 밀기 GBB -> BGB (B의 경우도 U와 방향이 반대임을 주의한다.)
> B' 가장 아랫줄을 왼쪽으로 한 칸 밀기 GBB -> BBG
> Q  Bye~를 출력하고 프로그램을 종료한다.
```

요구사항
- 처음 시작하면 초기 상태를 출력한다.
- 간단한 프롬프트 (CLI에서 키보드 입력받기 전에 표시해주는 간단한 글자들 - 예: CUBE> )를 표시해 준다.
- 한 번에 여러 문자를 입력받은 경우 순서대로 처리해서 매 과정을 화면에 출력한다.

# <br>구현 내용
## 구현 언어
python 언어를 사용하였습니다.

## 1단계에서 구현한 단어 밀기 함수 import
```python
from push_word import push_left, push_right
```
1단계에서 구현한 함수를 이용하여 해결하기 위해 import 하였습니다.

## plane_cube 클래스 정의
``` python
class plane_cube:
    def __init__(self):
        self.cube = [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']]
        self.print_cube()
        self.valid_commands = ["U", "U'", "R", "R'", "L", "L'", "B", "B'", "Q"]
        self.enter_commands()
```
1. 문제를 해결하기 위해 plane_cube 클래스를 정의하여 활용하였습니다.
1. 생성자에서 큐브 상태를 멤버로 선언하고, 문제에서 주어진 초기 큐브 상태로 초기화합니다.
1. 요구사항 첫 번째를 해결하기 위해 현재 큐브 상태를 출력하는 멤버 함수를 호출합니다.
1. 예외처리를 위한 유효한 명령어 리스트도 멤버로 선언합니다.
1. 이후 사용자로부터 입력을 받아 처리하는 멤버 함수를 호출합니다.

이후의 함수들은 모두 plane_cube 클래스의 멤버 함수입니다.
## print_cube() 함수
```python
def print_cube(self):
    for i in range(3):
        for j in range(3):
            print(self.cube[i][j], end=' ')
        print()
    print()
```
현재 큐브 상태를 담고 있는 멤버 `self.cube`를 참조하여 현재 큐브 상태를 출력합니다.

## enter_commands() 함수
```python
def enter_commands(self):
    while True:
        cmd = input('CUBE> ')
        if cmd == 'Q':
            print('Bye~')
            break
        for i in range(len(cmd)):
            if cmd[i] == "'":
                continue
            command = cmd[i]
            if i + 1 != len(cmd) and cmd[i+1] == "'":
                command += "'"
            if self.check(command) == True:
                self.process_command(command)
            else:
                print(command)
                print(f"잘못된 입력입니다. 입력은 {self.valid_commands} 만 가능합니다.")
                break
```
1. while문을 무한 loop로 만듭니다. 사용자가 `Q`를 입력해 종료할 때까지 입력을 받기 위함입니다.
1. 문제의 두 번째 요구사항인 `간단한 프롬프트를 화면에 표시하는 것`을 구현하기 위해 `input('CUBE> ')`를 통해 이를 해결하였습니다.
1. 사용자가 `Q`를 입력하였다면 화면에 `Bye~`를 출력하고 종료합니다.
1. 문제의 세 번째 요구사항인 `한 번에 여러 문자를 입력받은 경우 순서대로 처리해서 매 과정을 화면에 출력한다.`를 구현하기 위해 사용자가 입력한 명령어를 for 반복문을 이용하여 처리하였습니다.
1. 명령어는 `U'`처럼 `'`가 들어가는 경우를 처리해야 하므로, 현재 명령문이 전체 명령어의 마지막이 아니고 `i + 1 != len(cmd)`, 현재 명령문의 다음 명령문이 `'`인 경우 `cmd[i+1] == "'"`를 체크하여 명령문에 추가하였습니다.
1. 이후 유효한 명령어라면 멤버 함수인 `process_command()`를 이용해 큐브를 조작합니다.
1. 유효한 명령어가 아니라면 다시 사용자로 하여금 명령어를 다시 입력하도록 합니다.

## check() 함수
``` python
def check(self, command):
    return True if command in self.valid_commands else False
```
인자로 들어온 command가 클래스의 멤버인 `valid_commands` 리스트에 있으면 `True`를 return하고, 아니라면 `False`를 return합니다.

## process_command() 함수
``` python
def process_command(self, command):
    print(command)
    if command == "U":
        c = ''.join(self.cube[0])
        self.cube[0] = list(push_left(1, c))
    elif command == "U'":
        c = ''.join(self.cube[0])
        self.cube[0] = list(push_right(1, c))
    elif command == "R":
        c = ''.join([self.cube[i][-1] for i in range(3)])
        c = list(push_left(1, c))
        for i in range(3):
            self.cube[i][-1] = c[i]
    elif command == "R'":
        c = ''.join([self.cube[i][-1] for i in range(3)])
        c = list(push_right(1, c))
        for i in range(3):
            self.cube[i][-1] = c[i]
    elif command == "L":
        c = ''.join([self.cube[i][0] for i in range(3)])
        c = list(push_right(1, c))
        for i in range(3):
            self.cube[i][0] = c[i]
    elif command == "L'":
        c = ''.join([self.cube[i][0] for i in range(3)])
        c = list(push_left(1, c))
        for i in range(3):
            self.cube[i][0] = c[i]
    elif command == "B":
        c = ''.join(self.cube[-1])
        self.cube[-1] = list(push_right(1, c))
    elif command == "B'":
        c = ''.join(self.cube[-1])
        self.cube[-1] = list(push_left(1, c))
    self.print_cube()
```
1. 인자로 들어온 command에 따라 큐브를 조작합니다.
1. 가장 윗줄, 가장 아랫줄을 조작하는 `U`, `U'`, `B`, `B'`의 경우 윗줄, 아랫줄을 각각 `self.cube[0]`, `self.cube[-1]`로 받아와 `''.join()`을 통해 문자열로 만든 후, 문제 조건에 따라 `push_left()`와 `push_right()`에 인자로 넣어 처리합니다.
    - `U`는 가장 윗줄을 왼쪽으로 한 칸 밀어야 하므로 `push_left()` 해줍니다.
    - `U'`는 가장 윗줄을 오른쪽으로 한 칸 밀어야 하므로 `push_right()` 해줍니다.
    - `B`는 가장 아랫줄을 오른쪽으로 한 칸 밀어야 하므로 `push_right()` 해줍니다.
    - `B'`는 가장 아랫줄을 왼쪽으로 한 칸 밀어야 하므로 `push_left()` 해줍니다.
1. 가장 오른쪽 줄을 조작하는 `R`, `R'`의 경우는 `[self.cube[i][-1] for i in range(3)]`와 같이 리스트 컴프리헨션을 이용하여 가장 오른쪽 줄만을 가져옵니다. 이후 `2.`와 같이 큐브를 조작합니다.
    - `R`은 가장 오른쪽 줄을 위로 한 칸 밀어야 하므로 `push_left()` 해줍니다.
    - `R'`은 가장 오른쪽 줄을 아래로 한 칸 밀어야 하므로 `push_right()` 해줍니다.
1. 가장 왼쪽 줄을 조작하는 `L`, `L'`의 경우 역시 `3.`과 마찬가지로 리스트 컴프리헨션 `[self.cube[i][0] for i in range(3)]`을 이용하여 가장 왼쪽 줄을 가져와 큐브를 조작합니다.
    - `L`은 가장 왼쪽 줄을 아래로 한 칸 밀어야 하므로 `push_right()` 해줍니다.
    - `L'`은 가장 왼쪽 줄을 아래로 한 칸 밀어야 하므로 `push_left()` 해줍니다.

## 클래스 생성자 호출
```python
plane_cube()
```
클래스 생성자를 호출하여 구현한 내용을 동작하게 합니다.