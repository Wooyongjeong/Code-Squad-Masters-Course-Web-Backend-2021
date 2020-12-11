from push_word import push_left, push_right
from plane_cube import plane_cube
from time import time
from random import randrange, choice

class cube():
    def __init__(self):
        self.start_time = time() # 경과 시간 측정을 위해 시간 측정
        self.cube = [
            plane_cube('B').cube,
            plane_cube('W').cube, plane_cube('O').cube, plane_cube('G').cube, plane_cube('Y').cube,
            plane_cube('R').cube
        ]
        self.print_cube() # 큐브 상태 출력
        self.valid_commands = ["U", "U'", "L", "L'", "F", "F'", "R", "R'", "B", "B'", "D", "D'", "Q"] # 가능한 명령어 리스트
        self.mix_cube() # 큐브 무작위 섞기 함수
        self.enter_commands() # 사용자로부터 입력을 받는 함수

    def mix_cube(self):
        while True:
            want_random = input('큐브를 무작위로 섞으시겠습니까? (Y/N) > ')
            if want_random == 'Y':
                random_count = randrange(10, 20) # 10 ~ 20 중 랜덤한 숫자
                # 그 횟수만큼 가능한 명령어 리스트("Q"는 제외) 중 랜덤하게 실행
                print(f"{random_count}번 큐브를 섞습니다...")
                random_commands = [choice(self.valid_commands[:-1]) for _ in range(random_count)]
                for command in random_commands:
                    self.process_command(command)
                print("큐브 섞기 완료")
                self.print_cube()
                break
            elif want_random == 'N':
                break
            else:
                print('Y 또는 N으로 입력해주세요')

    # 큐브의 위쪽, 아랫쪽 부분을 출력하는 함수
    def print_one_cube(self, is_first=True):
        s = ''
        if is_first == True:
            cube_index = 0
        else:
            cube_index = -1
        for i in range(3):
            s += ' ' * 16
            for j in range(3):
                c = self.cube[cube_index]
                s += c[i][j] + ' '
            s += '\n'
        return s

    # 큐브의 옆면 4면을 출력하는 함수
    def print_four_cube(self, cube_index, i):
        s = ''
        for j in range(3):
            c = self.cube[cube_index]
            s += c[i][j] + ' '
        if cube_index != 4:
            s += ' ' * 5
        else:
            s += ' '
        return s

    # 큐브의 현재 상태를 호출하는 함수
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

    # 2차원 배열을 시계 방향으로 회전하는 함수. 출처: https://deepwelloper.tistory.com/117
    def rotate_clockwise(self, m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
        return ret

    # 2차원 배열을 반시계 방향으로 회전하는 함수. 출처: https://deepwelloper.tistory.com/117
    def rotate_counterclockwise(self, m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
        return ret

    # 위(Up)
    def up(self, clockwise=True):
        cube_string = ''
        rotating_planes = range(1, 5) # 윗쪽을 돌릴 때 돌아가는 큐브 면의 인덱스 
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                cube_string += c[0][j]
        if clockwise == True:
            self.cube[0] = self.rotate_clockwise(self.cube[0])
            cube_string = push_left(3, cube_string)
        else:
            self.cube[0] = self.rotate_counterclockwise(self.cube[0])
            cube_string = push_right(3, cube_string)
        index = 0
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                c[0][j] = cube_string[index]
                index += 1

    # 왼쪽(Left)
    def left(self, clockwise=True):
        cube_string = ''
        rotating_planes = [0, 2, 5, 4] # 왼쪽을 돌릴 때 돌아가는 큐브 면의 인덱스 
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for i in range(3):
                cube_string += c[i][0]
        if clockwise == True: # L
            self.cube[1] = self.rotate_clockwise(self.cube[1])
            cube_string = push_right(3, cube_string)
        else: # L'
            self.cube[1] = self.rotate_counterclockwise(self.cube[1])
            cube_string = push_left(3, cube_string)
        index = 0
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for i in range(3):
                c[i][0] = cube_string[index]
                index += 1

    # 앞쪽(Front)
    def front(self, clockwise=True):
        cube_string = ''
        rotating_planes = [0, 3, 5, 1] # 앞쪽을 돌릴 때 돌아가는 큐브 면의 인덱스
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                cube_string += c[-1][j]
        if clockwise == True: # F
            self.cube[2] = self.rotate_clockwise(self.cube[2])
            cube_string = push_right(3, cube_string)
        else: # F'
            self.cube[2] = self.rotate_counterclockwise(self.cube[2])
            cube_string = push_left(3, cube_string)
        index = 0
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                c[-1][j] = cube_string[index]
                index += 1

    # 오른쪽(right)
    def right(self, clockwise=True):
        cube_string = ''
        rotating_planes = [0, 2, 5, 4] # 오른쪽을 돌릴 때 돌아가는 큐브 면의 인덱스 
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for i in range(3):
                cube_string += c[i][-1]
        if clockwise == True: # R
            self.cube[3] = self.rotate_clockwise(self.cube[3])
            cube_string = push_right(3, cube_string)
        else: # R'
            self.cube[3] = self.rotate_counterclockwise(self.cube[3])
            cube_string = push_left(3, cube_string)
        index = 0
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for i in range(3):
                c[i][-1] = cube_string[index]
                index += 1

    # 뒤(Back)
    def back(self, clockwise=True):
        cube_string = ''
        rotating_planes = [0, 3, 5, 1] # 앞쪽을 돌릴 때 돌아가는 큐브 면의 인덱스
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                cube_string += c[0][j]
        if clockwise == True: # F
            self.cube[4] = self.rotate_clockwise(self.cube[4])
            cube_string = push_right(3, cube_string)
        else: # F'
            self.cube[4] = self.rotate_counterclockwise(self.cube[4])
            cube_string = push_left(3, cube_string)
        index = 0
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                c[0][j] = cube_string[index]
                index += 1

    # 아랫쪽(Down)
    def down(self, clockwise=True):
        cube_string = ''
        rotating_planes = range(1, 5) # 아랫쪽을 돌릴 때 돌아가는 큐브 면의 인덱스 
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                cube_string += c[-1][j]
        if clockwise == True:
            self.cube[-1] = self.rotate_clockwise(self.cube[-1])
            cube_string = push_left(3, cube_string)
        else:
            self.cube[-1] = self.rotate_counterclockwise(self.cube[-1])
            cube_string = push_right(3, cube_string)
        index = 0
        for cube_index in rotating_planes:
            c = self.cube[cube_index]
            for j in range(3):
                c[-1][j] = cube_string[index]
                index += 1

    # command에 따라 큐브를 조작하는 함수
    def process_command(self, command):
        if command == "U":
            self.up()
        elif command == "U'":
            self.up(clockwise=False)
        elif command == "L":
            self.left()
        elif command == "L'":
            self.left(clockwise=False)
        elif command == "F":
            self.front()
        elif command == "F'":
            self.front(clockwise=False)
        elif command == "R":
            self.right()
        elif command == "R'":
            self.right(clockwise=False)
        elif command == "B":
            self.back()
        elif command == "B'":
            self.back(clockwise=False)
        elif command == "D":
            self.down()
        elif command == "D'":
            self.down(clockwise=False)

    # command가 유효한 명령어인지 판단하는 함수
    def check(self, command):
        return True if command in self.valid_commands else False
    
    # 사용자로부터 입력을 받아 명령어를 처리하는 함수
    def enter_commands(self):
        while True:
            cmd = input('CUBE> ')
            if cmd == 'Q':
                end_time = time()
                elapsed_time = int(end_time - self.start_time)
                print(f"경과 시간: {elapsed_time // 60:02d}:{elapsed_time % 60:02d}")
                print("이용해주셔서 감사합니다. 뚜뚜뚜.")
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
                        self.print_cube()
                    command_count = 1
                else:
                    print(command)
                    print(f"잘못된 입력입니다. 입력은 {self.valid_commands} 만 가능합니다.")
                    break

cube()