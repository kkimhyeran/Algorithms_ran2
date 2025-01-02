import math
def parking_time(in_time, out_time):
    in_time_hh, in_time_mm = map(int, in_time.split(':'))
    out_time_hh, out_time_mm = map(int, out_time.split(':'))
    
    return (out_time_hh - in_time_hh) * 60 + (out_time_mm - in_time_mm)

def solution(fees, records):
    
    # 1. 차량별 IN-OUT 데이터 정제
    car_in_out_dict = {}
    for record in records:
        time, car_number, type = record.split(' ')
        
        if car_number not in car_in_out_dict.keys():
            car_in_out_dict[car_number] = [[], []]
            
            # IN
            if type == 'IN':
                car_in_out_dict[car_number][0].append(time)
            # OUT
            else:
                car_in_out_dict[car_number][1].append(time)
        else:
            # IN
            if type == 'IN':
                car_in_out_dict[car_number][0].append(time)
            # OUT
            else:
                car_in_out_dict[car_number][1].append(time)
    
    # 2. 차량별 누적 시간 계산
    cumsum_dict = {}
    for car, times in car_in_out_dict.items():
        
        if len(times[0]) != len(times[1]):
            car_in_out_dict[car][1].append("23:59")
            
        # IN 한 것 만큼 계산
        cumsum_time = 0
        for i in range(len(times[0])):
            cumsum_time += parking_time(times[0][i], times[1][i])

        cumsum_dict[car] = cumsum_time
    
    # 차량 번호 오름차순 정렬
    # cumsum_dict.sort(reverse = True)
    cumsum_dict = dict(sorted(cumsum_dict.items(), reverse=False))

    # 3. 차량별 주차요금 계산하기
    print(cumsum_dict)
    answer = []
    for car, cumsum_time in cumsum_dict.items():
        # 기본 시간 초과 확인
        if cumsum_time > fees[0]:
            # 기본요금 + 초과 시간 단위요금
            
            # 초과시간 요금 구하기
            add_time = cumsum_time - fees[0]
            add_fee = math.ceil(add_time / fees[2]) * fees[3]
            total_fee = fees[1] + add_fee
            answer.append(total_fee)
        else:
            answer.append(fees[1])
            
    return answer