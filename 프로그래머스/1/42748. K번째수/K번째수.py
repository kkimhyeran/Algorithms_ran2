def solution(array, commands):
    
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        tmp_array = array[i-1:j]
        tmp_array.sort()
        
        answer.append(tmp_array[k-1])
        
    return answer