def solution(park, routes):
    current = [0, 0] # 시작위치
    ismove = True
    find = False
    for i, row in enumerate(park):
        for j, col in enumerate(row):
            if col == 'S':
                current[0] = i
                current[1] = j
                find = True
                break
        if find == True:
            break
    movement = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    for route in routes:
        direction, moving = route.split()
        moving = int(moving)
        going = 0
        going = current.copy()
        for i in range(moving): # 가는 길에 방해물이 있거나 벗어나는지 확인
            going[0] += movement[direction][0]
            going[1] += movement[direction][1]
            if going[0] < 0 or going[0] > len(park) - 1:
                ismove = False
                break
            if going[1] < 0 or going[1] > len(park[0]) - 1:
                ismove = False
                break
            if park[going[0]][going[1]] == "X":
                ismove = False
                break
        if ismove == True:
            current = going
        ismove = True
        print(current)
    return current
park = [ "SOO",
         "OXX",
         "OOO" ]
routes = ["E 2","S 2","W 1"]
print(solution(park, routes))