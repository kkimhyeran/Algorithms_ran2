from datetime import datetime

def solution(data, ext, val_ext, sort_by):
    meta = ['code','date', 'maximum', 'remain']
    
    # ext : 정보를 추출할 기준
    # val_ext : 기준에 대한 값
    # sort_by : 정렬 기준
    
    idx = meta.index(ext)
    
    answer = []
    
    # 1. 정보 추출
    for d in data:
        
        # 날짜 기준인 경우
        if ext == 'date':
            if datetime.strptime(str(d[idx]),"%Y%m%d") < datetime.strptime(str(val_ext),"%Y%m%d"):
                answer.append(d)
                
        # code, maximum, remain
        else:
            if d[idx] < val_ext:
                answer.append(d)
        
    # 2. 정렬
    sort_idx = meta.index(sort_by)
    
    answer = sorted(answer, key = lambda x:x[sort_idx]) 
    
    return answer