from push_word import push_left, push_right

# plane_cube 클래스
class plane_cube:
    def __init__(self):
        self.cube = [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']] # 초기 큐브 상태
        self.print_cube() # 현재 큐브 상태를 출력하는 함수
        self.valid_commands = ["U", "U'", "R", "R'", "L", "L'", "B", "B'"] # 유효한 명령어 리스트
        self.enter_commands() # 사용자로부터 입력을 받아 처리하는 함수
    
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
                    print(f"잘못된 입력입니다. 입력은 {self.valid_commands}만 가능합니다.")
                    break