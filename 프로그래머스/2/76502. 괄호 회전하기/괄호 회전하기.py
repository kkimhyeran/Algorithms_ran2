from collections import deque

def right_strings(s):
    stack = []
    for i in s:
        if (i == '(') or (i == '{') or (i == '['):
            stack.append(i)
        elif stack and i == ')' and stack[-1] == '(':
            stack.pop()
        elif stack and i == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and i == ']' and stack[-1] == '[':
            stack.pop()     
        else:
            return 0

    if len(stack) == 0:
        return 1
    else:
        return 0
    
def solution(s):
    
    # 1. 괄호 문자열 길이만큼 회전하기
    answer = 0
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        chk = right_strings(tmp)
        answer += chk
    return answer