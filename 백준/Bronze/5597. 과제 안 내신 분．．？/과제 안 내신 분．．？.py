
submit_list = [i for i in range(1,31)]

for _ in range(28):
    submit_number = int(input())
    submit_list.remove(submit_number)
    
[print(student) for student in submit_list]


