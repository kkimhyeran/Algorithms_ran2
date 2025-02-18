def solution(keymap, targets):
    
    # 1. keymap 속 자판별 최소 누른 횟수 미리 구하기
    keymap_dict = {}
    for key in keymap:
        for idx, s in enumerate(key):
            if s not in keymap_dict.keys():
                keymap_dict[s] = idx + 1
            else:
                keymap_dict[s] = min(keymap_dict[s], idx + 1)
    
    # 2. 자판 누르기
    answer = []
    for target in targets:
        rslt = 0
        
        for char in target:
            if char in keymap_dict:
                rslt += keymap_dict[char]
            else:
                rslt = -1
                break

        answer.append(rslt)

    
    return answer