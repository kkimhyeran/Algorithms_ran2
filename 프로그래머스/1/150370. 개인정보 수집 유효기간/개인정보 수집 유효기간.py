from datetime import datetime

def solution(today, terms, privacies):
    # 1. 약관 별 유효기간 보존 기간 정리
    valid_terms = {}
    for t in terms:
        valid_terms[t[0]] = int(t[2:])  # {약관 : 유효기간}
        
    answer = []
    today = datetime.strptime(today, '%Y.%m.%d')
    for idx, privacy in enumerate(privacies):
        
        # today - 개인정보 수집일자
        date = datetime.strptime(privacy[:10], '%Y.%m.%d')
        diff_month = (today.year - date.year) * 12 + today.month - date.month
        diff_day = today.day - date.day
        
        if diff_day < 0:
            diff_month -= 1
            diff_day += 28
        
        # 유효기간 지났는지 확인
        if diff_month >= valid_terms[privacy[11]]:
            answer.append(idx + 1)
            
    return answer