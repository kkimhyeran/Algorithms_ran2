'''
@ No        : 1092
@ Title     : 배
@ Subject   : 그리디, 정렬

@ 입력값
    - n : 크레인 대수
    - crain_weights : 크레인 별 무게 제한
    - m : 박수 개수
    - box_weights : 박스 별 무게
@ 출력값
    - 박스를 옮기는데 소요된 시간
    - 박스 하나라도 옮길 수 없는 경우 -1 출력
'''


n = int(input())
crain_weights = list(map(int, input().split()))

m = int(input())
box_weights = list(map(int, input().split()))



crain_weights.sort(reverse=True)
box_weights.sort(reverse=True)

time = 0
if crain_weights[0] < box_weights[0]:
    time = -1
else:
    while box_weights:
        for crain in crain_weights:
            if box_weights and crain < box_weights[-1]:
                continue
            else:
                for box in box_weights:
                    if box <= crain:
                        box_weights.remove(box)
                        break
        # 크레인을 한바퀴 탐색할때 마다
        time += 1


print(time)














