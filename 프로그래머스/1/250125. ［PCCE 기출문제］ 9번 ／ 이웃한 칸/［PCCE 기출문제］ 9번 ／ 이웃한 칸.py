def solution(board, h, w):
    answer = 0
    
    # 1. board[h][w] 색깔 확인하기
    color = board[h][w]
    # 2. 2차원 배열에서 board[h][w] 좌우에 같은 색 칸 갯수 세기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    width = len(board)
    length = len(board[0])
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        
        if 0 <= nx < width and 0 <= ny < length:
            if board[nx][ny] == color:
                answer += 1
    return answer