import re
def split_file(file, i):
        # 정규식을 사용하여 HEAD, NUMBER, TAIL 추출
        match = re.match(r"([a-zA-Z\s.-]+)(\d+)(.*)", file)
        if match:
            head, number, tail = match.groups()
            return [head.lower(), int(number), i]  # 원본 파일명 유지
        return ["", 0, i] # 매칭 실패 시 대비

    
def solution(files):
    # 1. 파일명 head, number, tail 로 자르기
    files_dict = {file: split_file(file, i) for i, file in enumerate(files)}
            
#     files_dict = {}
#     for i in range(len(files)):
#         key = heads[i] + numbers[i] + files[i]
#         files_dict[key] = [heads[i].lower(), int(numbers[i]), i]
    

    # 2. 정렬
    answer = sorted(files_dict.keys(), key= lambda x: (files_dict[x][0], files_dict[x][1], files_dict[x][2]))

    return answer