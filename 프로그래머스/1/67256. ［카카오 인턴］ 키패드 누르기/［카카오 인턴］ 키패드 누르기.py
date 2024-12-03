keypads = [[1, 2, 3],
               [4, 5, 6], 
               [7, 8, 9], 
               ['*', 0,'#']]

def current_position(target):
    for i in range(len(keypads)):
        for j in range(len(keypads[0])):
        
            if keypads[i][j] == target:
                return [i, j]
            
    
def solution(numbers, hand):
    
    left_list = [1, 4, 7]
    right_list = [3, 6, 9]
    mid_list = [2, 5, 8, 0]
    
    
    # 왼손, 오른손 시작 위치
    left = current_position('*')
    right = current_position('#')
        
    
    # 2. 키패드 누르기
    answer = ''
    for num in numbers:
        # 1. 왼손
        if num in left_list:
            answer += 'L'
            left = current_position(num)
        elif num in right_list:
            answer += 'R'
            right = current_position(num)
        else:
            # 1. 거리 계산하기
            num_pos = current_position(num)
            
            left_dist = abs(num_pos[0]-left[0]) + abs(num_pos[1]-left[1])
            right_dist = abs(num_pos[0]-right[0]) + abs(num_pos[1]-right[1])
            
            # 왼손이 더 가까우면
            if left_dist < right_dist:
                answer += 'L'
                left = current_position(num)
            elif left_dist > right_dist:
                answer += 'R'
                right = current_position(num)
            else:
                
                if hand == 'left':
                    answer += 'L'
                    left = current_position(num)
                else:
                    answer += 'R'
                    right = current_position(num)
                
        
    
    return answer