def solution(id_list, report, k):
    
    # 1. 필요한 변수 생성
    report_dict = {i: [] for i in id_list} # id 별로 신고한 id 저장할 변수
    reported_dict = {i: 0 for i in id_list} # 신고당한 id 회수 저장
    
    # 2. 유저별 신고 정보 정리
    for r in report:
        source, target = list(r.split(' '))
        
        # 처음 신고하는 유저이면
        if target not in report_dict[source]:
            report_dict[source].append(target)
            reported_dict[target] += 1
            
    # print(reported_dict)
    # 3. 신고 횟수가 2회 이상인 id만 추출
    stop_id = {key : val for key, val in reported_dict.items() if val >= k}
    # print(stop_id)
    # print(report_dict)
    
    # 4. 
    answer = [0]* len(id_list)
    for id in stop_id.keys():
        for key, val in report_dict.items():
            if id in val:
                idx = id_list.index(key)
                answer[idx] += 1

    return answer