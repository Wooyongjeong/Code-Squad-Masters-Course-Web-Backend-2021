from push_word import push_left, push_right

# plane_cube 클래스
class plane_cube:
    def __init__(self, color=None):
        if color is None:
            self.cube = [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']] # 초기 큐브 상태
        else:
            self.cube = [[color for _ in range(3)] for _ in range(3)]
        self.valid_commands = ["U", "U'", "R", "R'", "L", "L'", "B", "B'", "Q"] # 유효한 명령어 리스트
    
    # 현재 큐브 상태를 출력하는 함수
    def print_cube(self):
        for i in range(3):
            for j in range(3):
                print(self.cube[i][j], end=' ')
            print()
        print()
    
    # command가 유효한 명령어인지 판단하는 함수
    def check(self, command):
        return True if command in self.valid_commands else False
    
    # command에 따라 큐브를 조작하는 함수
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
    
    # 사용자로부터 입력을 받아 처리하는 함수
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
