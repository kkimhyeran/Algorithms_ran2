def solution(players, callings):
    
    players_dict = {player:i for i, player in enumerate(players)} # 딕셔너리 컴프리헨션 
    
    for call in callings:
        now_idx = players_dict[call]
        
        # players 리스트 업데이트
        players[now_idx] = players[now_idx-1]
        players[now_idx-1] = call
        

        # 딕셔너리 업데이트
        players_dict[players[now_idx]] = now_idx
        players_dict[call] = now_idx-1
    return players