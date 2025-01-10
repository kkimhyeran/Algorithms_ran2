def solution(elements):
    # 1. 각 길이별로 부분 수열 모두 구하기
    n = len(elements)
    elements += elements[:-1]
    
    rslt = []
    for i in range(1, n+1):
        partitial_list = [sum(elements[j:j+i]) for j in range(n)]
        rslt.extend(partitial_list)

    return len(set(rslt))