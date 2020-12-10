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