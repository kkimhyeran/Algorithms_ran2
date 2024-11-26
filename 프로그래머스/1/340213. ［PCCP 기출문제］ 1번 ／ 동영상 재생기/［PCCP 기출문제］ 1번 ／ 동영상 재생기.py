def solution(video_len, pos, op_start, op_end, commands):
    
    # 1. 시간 초단위로 전부 변환하기
    video_mm, video_ss = map(int, video_len.split(':'))
    pos_mm, pos_ss = map(int, pos.split(':'))
    op_start_mm, op_start_ss = map(int, op_start.split(':'))
    op_end_mm, op_end_ss = map(int, op_end.split(':'))
    
    video_len = video_mm*60 + video_ss
    pos = pos_mm*60 + pos_ss
    op_start = op_start_mm*60 + op_start_ss
    op_end = op_end_mm*60 + op_end_ss
    
    # 명령어 수행 전에 현재 위치가 오프닝 구간이면 오프닝 마지막으로 이동하기
    if op_start <= pos < op_end:
            pos = op_end
            
    # 2. 명령어 수행하기
    for command in commands:
        if command == 'prev':
            pos -= 10
            
            # 만약 영상 시작 전보다 이전이면 영상 시작점으로 이동
            if pos < 0:
                pos = 0
        else:
            pos += 10
            
            # 영상 끝을 넘어가면 영상 끝 시점으로 이동
            if pos > video_len:
                pos = video_len
            
        # 오프닝 구간 확인
        if op_start <= pos < op_end:
            pos = op_end
            
    
    # 3. 현재 시간 분,초로 다시 변환
    pos_mm = pos // 60
    pos_ss = pos % 60
        
    answer = str(pos_mm).rjust(2, '0')+ ':' + str(pos_ss).rjust(2, '0')
    return answer