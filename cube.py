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

