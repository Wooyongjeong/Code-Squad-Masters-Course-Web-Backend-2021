from plane_cube import plane_cube

class cube():
    def __init__(self):
        self.cube = [
            plane_cube('B'),
            plane_cube('W'), plane_cube('O'), plane_cube('G'), plane_cube('Y'),
            plane_cube('R')
        ]
        self.print_cube() # 큐브 상태 출력
        self.valid_commands = ["U", "U'", "L", "L'", "F", "F'", "R", "R'", "B", "B'", "D", "D'", "Q"] # 가능한 명령어 리스트
        self.enter_commands() # 사용자로부터 입력을 받는 함수

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
                s += c.cube[i][j] + ' '
            s += '\n'
        return s

    # 큐브의 옆면 4면을 출력하는 함수
    def print_four_cube(self, cube_index, i):
        s = ''
        for j in range(3):
            c = self.cube[cube_index]
            s += c.cube[i][j] + ' '
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
    
    # command에 따라 큐브를 조작하는 함수
    def process_command(self, command):
        print(command)
        if command == "U":
            up()
        elif command == "U'":
            self.up(reverse=True)
        elif command == "L":
            self.left()
        elif command == "L'":
            self.left(reverse=True)
        elif command == "F":
            self.front()
        elif command == "F'":
            self.front(reverse=True)
        elif command == "R":
            self.right()
        elif command == "R'":
            self.right(reverse=True)
        elif command == "B":
            self.back()
        elif command == "B'":
            self.back(reverse=True)
        elif command == "D":
            self.down()
        elif command == "D'":
            self.down(reverse=True)

    # command가 유효한 명령어인지 판단하는 함수
    def check(self, command):
        return True if command in self.valid_commands else False
    
    # 사용자로부터 입력을 받아 명령어를 처리하는 함수
    def enter_commands(self):
        while True:
            cmd = input('CUBE> ')
            if cmd == 'Q':
                print('Bye~')
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
                        self.process_command(command)
                    command_count = 1
                else:
                    print(command)
                    print(f"잘못된 입력입니다. 입력은 {self.valid_commands} 만 가능합니다.")
                    break