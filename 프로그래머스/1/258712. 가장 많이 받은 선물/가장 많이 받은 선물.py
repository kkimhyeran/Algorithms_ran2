def solution(friends, gifts):
    
    
    # 1. 주고 받은 선물 2차원 초기 리스트 변순 선언
    # 0이면 아무것도 주고 받지 않은 상태임.
    prsnt_list = [[0]*len(friends) for i in range(len(friends))]

    for gift in gifts:

        give, take = gift.split()[0], gift.split()[1]
        row = friends.index(give) # 준 사람 인덱스 값
        col = friends.index(take) # 받은 사람 인덱스 값
        prsnt_list[row][col] += 1 # 주고 받은 선물 2차원 리스트 업데이트


    # 2. 준 선물, 받은 선물 개수, 선물지수 구하기

    give_sum_list = []
    take_sum_list = []
    prsnt_point_list = []

    for i in range(len(prsnt_list)):
        # 2.1) 준 선물은 2차원 배열 각 행 합
        give_sum_list.append(sum(prsnt_list[i]))

        # 2.2) 받은 선물은 2차원 배열 각 열의 합
        take_temp_sum = [prsnt_list[row][i] for row in range(len(prsnt_list))]
        take_sum_list.append(sum(take_temp_sum))

        # 2.3) 선물 지수: 준선물 - 받은 선물
        prsnt_point_list.append(give_sum_list[i] - take_sum_list[i])



    # 3. 각 사람별로 이번달에 받는 선물 개수 구하가
    # 이전에 주고 받은 선물과 선물지수표를 기반으로 계산

    now_take_prsnt_list = []

    for i in range(len(prsnt_list)):

        # 받을 선물 수 저장 변수
        cnt = 0

        for j in range(len(prsnt_list[i])):

            # 3.1) 내가 저번달에 상대방보다 선물을 더 줬으면 이번달에는 내가 선물을 받는다.
            if prsnt_list[j][i] < prsnt_list[i][j]:
                cnt += 1

            # 3.2) 선물 개수가 똑같다면 선물지수가 더 큰사람이 선물을 받는다.
            # 선물을 주고 받지 않더라도 해당 조건은 동일하다.
            elif prsnt_list[j][i] == prsnt_list[i][j] and prsnt_point_list[i] > prsnt_point_list[j]:
                cnt += 1

        # 각 사람별로 받는 선물 수 저장
        now_take_prsnt_list.append(cnt)

    answer = max(now_take_prsnt_list)
    return answer



