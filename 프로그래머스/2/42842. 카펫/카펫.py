def solution(brown, yellow):
    
    # 1. 최소공약수 구하기
    area = brown + yellow 
    numbers = [i for i in range(1, area + 1) if area % i == 0]

            
    # 2. 최소공약수 중 곱해서 총 면적이 되는 짝 구하기
    candidates = []
    for num1 in numbers:
        for num2 in numbers:
            if num2 <= num1 and num1 * num2 == area:
                candidates.append([num1, num2])
    
    
    # 3. 면적이 될 수 있는 모든 경우 탐색
    for candidate in candidates:
        tmp_carpet = [[0]*candidate[0] for _ in range(candidate[1])]
        
        # 맨 윗줄 > 맨 아랫 줄 > 양 옆 채운 후, 남아있는 칸이 yellow 개수랑 같으면 return
        # 맨 윗줄, 아랫줄 채우기
        for i in range(candidate[0]):
            tmp_carpet[0][i] = 'B'
            tmp_carpet[candidate[1]-1][i] = 'B'
            
        # 양옆 채우기
        for j in range(candidate[1]):
            tmp_carpet[j][0] = 'B'
            tmp_carpet[j][candidate[0]-1] = 'B'
            
        # brown 개수 확인
        brown_cnt = sum(row.count('B') for row in tmp_carpet)
        yellow_cnt = sum(row.count(0) for row in tmp_carpet)

        
            
        if brown_cnt == brown and yellow_cnt == yellow:

            return candidate

    