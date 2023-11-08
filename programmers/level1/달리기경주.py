'''
    단순 swap하면 시간 뻑남
    바로 접근 가능한 dict를 이용하여 풀어야함
    1. dict에 키:선수 이름 깂:등수로 생성
    2. 불린 선수을 dict로 접근하여 해당 선수의 등수를 저장
    3. players에 저장한 등수를 이용해 swap
    4. players에 저장한 등수로 접근하여 키를 통해 다시 저장한 등수를 dict에 저장
'''
def solution(players, callings):
    state = {player: rank for rank, player in enumerate(players)}
    print(state)
    for call in callings:
        idx = state[call]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        state[players[idx]] = idx
        state[players[idx - 1]] = idx - 1
    return players
players = input().split()
callings = input().split()
print(solution(players, callings))
