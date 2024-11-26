def check_area(i, j, mat, park):
    if i+mat > len(park) or j+mat>len(park[0]):
        return False
    
    for r in range(i, i+mat):
        for c in range(j, j+mat):
            if park[r][c] != "-1":
                return False
    return True
    
def solution(mats, park):
    
    # 1. mats 내림차순 정렬
    mats.sort(reverse = True)
    
    # 2. park 0부터 ~ mats 크기 영역 탐색
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if check_area(i, j, mat, park):
                    return mat
    return -1 