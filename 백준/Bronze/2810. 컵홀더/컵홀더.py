n = int(input())
seats = input()

# 커플석 수만큼 컵홀더가 없다.
cup_holder = seats.count('LL')

if cup_holder <= 1 :
    print(len(seats))
else :
    print(len(seats) - cup_holder + 1)
