def solution(name, yearning, photo):
    
    # 1. 사람별 추억점수 매핑 
    yearing_points_dict = {}
    for i in range(len(name)):
        yearing_points_dict[name[i]] = yearning[i]
    
    # 2. 사진 속 추억 점수 세기
    answer = []
    
    for pht in photo:
        point = 0 # 사진 속 추억점수 저장 변수
        
        for p in pht:
            if p in yearing_points_dict.keys():
                point += yearing_points_dict[p]
        answer.append(point)
    
    return answer