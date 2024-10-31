def solution(s, skip, index):
    # 1. skip 문자 지우기
    eng_str_list = [i for i in 'abcdefghijklmnopqrstuvwxyz' if i not in skip]
    
    # 2. 암호 해독
    answer = ''
    for i in s:
        #index 나머지로 구하기
        answer += eng_str_list[(eng_str_list.index(i) + index) % len(eng_str_list)]
        
    return answer