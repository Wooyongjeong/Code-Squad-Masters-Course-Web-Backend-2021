from push_word import push_left, push_right

# plane_cube 클래스
class plane_cube:
    def __init__(self):
        self.cube = [['R', 'R', 'W'], ['G', 'C', 'W'], ['G', 'B', 'B']] # 초기 큐브 상태
        self.print_cube() # 현재 큐브 상태를 출력하는 함수
        self.enter_commands() # 사용자로부터 입력을 받아 처리하는 함수
    
