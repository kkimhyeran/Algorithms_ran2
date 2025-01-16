def solution(wallpaper):
    
    # 1. 바탕화면 좌표화 
    matrix = []
    for file in wallpaper:
        matrix.append(list(file))
    
    # 2. 각 좌표별 위치값 구하기
    rows = []
    columns = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # 파일이 있는 좌표이면
            if matrix[i][j] == '#':
                rows.append(i)
                columns.append(j)

    
    # 3.S, E 위치 구하기
    S = [min(rows), min(columns)]
    E = [max(rows)+1, max(columns)+1]
    
    
    answer = S + E
    return answer