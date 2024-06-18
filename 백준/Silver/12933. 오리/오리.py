cry_duck = input()
# cry_duck = 'quackqauckquack'

# 오리 수를 확인 할 수 없는 경우 종료
if len(cry_duck) % 5 != 0:
    print(-1)
    exit()



sound_order = 'quack'
duck_cnt = 0
check_sound_list = [0] * len(cry_duck)


# 해당 문자를 모두 확인할 때 까지 반복문
for i in range(len(cry_duck)):
    if cry_duck[i] == 'q' and check_sound_list[i] == 0:
        j = 0
        first_duck = 0


        for i in range(i, len(cry_duck)):
            if cry_duck[i] == sound_order[j] and check_sound_list[i] == 0:
                # 해당 글자는 확인 완료 0 > 1 로 변경
                check_sound_list[i] = 1
                # 울음 소리 글자 다음 순서 확인 위해 +1
                j += 1


                # 울음소리 마지막 글자 and 아직 오리 수에 포함이 안된거면
                # 오리 마리 수에 업데이트
                if cry_duck[i] == 'k':
                    j = 0
                    if first_duck == 0:
                        duck_cnt += 1
                        first_duck = 1 # 현재 울음소리 오리 확인 완료


if duck_cnt == 0 or check_sound_list.count(0) >= 1:
    print(-1)

else:
    print(duck_cnt)