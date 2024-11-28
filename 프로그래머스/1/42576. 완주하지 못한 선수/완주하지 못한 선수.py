def solution(participant, completion):
    
    # 1. dict
    participant_dict = {}
    for p in participant:
        if p not in participant_dict.keys():
            participant_dict[p] = 1
        else:
            participant_dict[p] = participant_dict[p] + 1
    
    for c in completion:
        participant_dict[c] -= 1

    for c, i in participant_dict.items():
        if i != 0:
            return c
