from collections import deque

def solution(bandage, health, attacks):
    
    t, x, y = bandage
    max_health = health
    end_time = attacks[-1][0]
    attacks_dict = {attack[0]:attack[1] for attack in attacks}
    print(attacks_dict)
    # 연속적으로 t만큼 체력 회복하지는 확인
    chk_t = 0
    
    for i in range(end_time + 1):
        
        # 공격 시간이면
        if i in attacks_dict.keys():
            # print(health)
            # print(attacks_dict[i])
            health -= attacks_dict[i]
            chk_t = 0
            
            # 체력 0이하면 -1 
            if health <= 0:
                return -1
            
            # print('시간: {}'.format(i))
            # print('health: {}'.format(health))
            continue # 공격 당했으면 체력회복 할 필요 없음
        
        # 공격 시간이 아니면 체력 회복
        chk_t += 1
        health += x
        
        # 추가 회복
        if chk_t == t:
            health += y
            chk_t = 0
        
        health = min(health, max_health)
    return health