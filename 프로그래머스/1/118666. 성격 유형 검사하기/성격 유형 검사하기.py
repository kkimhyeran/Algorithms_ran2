def solution(survey, choices):
    
    # 1. 성격 유형별 점수 저장 dict
    prsn_dict = {'R':0, 'T':0, 'C':0, 'F':0, 
                 'J':0, 'M':0, 'A':0, 'N':0}
    
    points = [3, 2, 1, 0, 1, 2, 3]
    
    # 2. 성격 유형 점수 계산
    for i, s in enumerate(survey):
        
        # 선택 1 ~ 3
        if choices[i] <=3:
            prsn_dict[s[0]] = prsn_dict[s[0]] + points[choices[i]-1]
        # 선택 5 ~ 6
        elif choices[i] >= 5 and choices[i] <=7:
            prsn_dict[s[1]] = prsn_dict[s[1]] + points[choices[i]-1]
            
            
    # 3. 리스트로 변환
    prsn_list = [[key, value] for key, value in prsn_dict.items()] 
    
    
    # 4. 결과 출력
    answer = ''
    for i in range(0, 8, 2):
        
        type_list = prsn_list[i:i+2]
        type_list.sort(key=lambda x:(-x[1], x[0]))
        
        answer+= type_list[0][0]
        
    
  
    return answer