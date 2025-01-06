# 2x2 같은 블록인지 확인하는 함수
def check_block(now, i, j, matrix, n, m):
    for x in range(i, i+2):
        for y in range(j, j+2):
            # 칸 범위 확인
            if 0 <= x < m and 0 <= y < n:
                # 현재 칸이 기준 블록이랑 같으면
                if matrix[x][y] != now:
                    return False
    return True

# 삭제 블록 표시
def visited_block(now, i, j, visited, n, m):
    for x in range(i, i+2):
        for y in range(j, j+2):
            # 칸 범위 확인
            if 0 <= x < m and 0 <= y < n:
                visited[x][y] = True
            

def solution(m, n, board):
    
    # 1. 프렌즈 블록 2차원 리스트에 저장
    matrix = [list(board[i]) for i in range(m)]
    
    total_removed_cnt = 0
    while True:
        
        any_removed = False
        
        # 2. 각 칸별로 2x2 같은 모양이 있는지 확인
        visited = [[False]*n for i in range(m)]
        for i in range(m):
            for j in range(n):

                if matrix[i][j] == '':
                    continue

                if i < m-1 and j < n-1:
                    now = matrix[i][j]

                    # 2x2 가 모두 같은 블록이면
                    if check_block(now, i, j, matrix, n, m):
                        any_removed = True
                        # visited 처리
                        visited_block(now, i, j, visited, n, m)
        if not any_removed:  # 더 이상 삭제할 블록이 없으면 종료
            break
            
        # 3. 삭제 대상 블록 지우기
        for i in range(m):
            for j in range(n):
                if visited[i][j] == True:
                    matrix[i][j] = ''
                    total_removed_cnt += 1
                    

        # 4. 빈 블록 채우기
        for j in range(n):
            blocks = [matrix[i][j] for i in range(m) if matrix[i][j] != '']
            
            for i in range(m - len(blocks)):
                matrix[i][j] = ''
                
            for i in range(m - len(blocks), m):
                matrix[i][j] = blocks[i - (m - len(blocks))]
    
    return total_removed_cnt