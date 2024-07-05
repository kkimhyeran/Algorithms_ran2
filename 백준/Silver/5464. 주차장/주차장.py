'''
@ No: 5464
@ Title: 주차장
@ key Point: 큐 자료구조 사용

@ 입력값 :
    - n : 주차 공간 개수
    - m : 차량 대수
    - price_list : 주차 공간 별 단위 무게 당 요금
    - weight_list : 차량 s번의 무게
    - order_list : 주차장 출입 순서 (양수면 들어 오는 것, 음수면 나가는 차량)

@ 출력값 :
    - 총 요금

@ 조건 :
    - 빈 공간이 없으면 대기한다.
    - 빈 공간이 여러 대 이면 가장 번호가 작은 주차 공간에 주차한다.
    - 여러 대의 차량이 한 꺼번에 들어 오면 대기하고, 순서대로 주차한다.
'''


from collections import deque

# n, m = 2, 4
n, m = map(int, input().split())

price_list = [int(input()) for _ in range(n)]
# price_list = [5, 2]

weight_list = [int(input()) for _ in range(m)]
# weight_list = [100, 500, 1000, 2000]

order_list = [int(input()) for _ in range(2*m)]
# order_list = [3, 1, 2, 4, -1, -3, -2, -4]
total_sales = 0


# 주차장
car_space = [0 for _ in range(n)]
wait_queue = deque()

for car in order_list:
    # 일단 차가 들어오면 대기한다.
    if car > 0:
        wait_queue.append(car)

        while wait_queue:
            if 0 in car_space:
                now_car = wait_queue.popleft()
                empty_idx =  car_space.index(0)
                car_space[empty_idx] = now_car
                total_sales += weight_list[now_car-1] * price_list[empty_idx] # 차량 무계 * 단위 무게당 요금
            else:
                break

    # 나가는 차
    else:
        idx = car_space.index(abs(car))
        car_space[idx] = 0 # 차가 나가면 0으로 변경

        if wait_queue:
            now_car = wait_queue.popleft()
            empty_idx = car_space.index(0)
            car_space[empty_idx] = now_car
            total_sales += weight_list[now_car - 1] * price_list[empty_idx]


print(total_sales)
