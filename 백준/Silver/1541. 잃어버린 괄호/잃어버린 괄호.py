expresions = input().split('-')

value_list = []
for exp in expresions:
    temp_list = exp.split('+')

    temp_val = 0
    for i in temp_list:
        temp_val += int(i)

    value_list.append(temp_val)
rslt = value_list[0]
for j in range(1, len(value_list)):
    rslt -= value_list[j]
    
print(rslt)