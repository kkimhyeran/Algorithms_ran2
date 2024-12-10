# 총 음악 재생 시간 구하기
def playing_time(start, end):
    start_hh, start_mm = map(int, start.split(':'))
    end_hh, end_mm = map(int, end.split(':'))
    
    return (end_hh - start_hh) * 60 + (end_mm - start_mm)
    
# 총 음악 재생 시간에 따른 음악 추출
def get_melody(time, sound):
    sounds = ''
    while len(sounds) < time:
        sounds += sound
        
    return sounds[:time]
            
    
def solution(m, musicinfos):
    
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "b")
    
    # 각 노래별 재생시간에 따라서 총 음 길이 추출
    musicinfos_dict = {}
    for i, musicinfo in enumerate(musicinfos):
        musicinfo_list = musicinfo.split(',')
        total_time = playing_time(musicinfo_list[0], musicinfo_list[1])
        
        
        # 노래 제목
        title = musicinfo_list[2]
        
        # 음 데이터 전처리
        melody = musicinfo_list[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "b")
        
        total_melody = get_melody(total_time, melody)
        musicinfos_dict[title] = [total_melody,total_time, i] # 멜로디, 재생시간, 입력순서
    
    
    # 정렬 음악 재생시간 순으로 내림차순 (같은 제목 음악 우선순위 처리때문에)
    musicinfos_sort_dict = dict(sorted(musicinfos_dict.items(), 
                                       key= lambda x:(-x[1][1], x[1][2])))
    
    print(musicinfos_sort_dict)
    # 2. 멜로디가 들어있는 음악 제목 찾기
    answer = "(None)"
    for key, value in musicinfos_sort_dict.items():
        if m in value[0]:
            return key

    
    return answer