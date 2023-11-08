def solution(demand, tree):
    start = 1
    end = max(tree)
    middle = (start+end)//2
    while start <= end:
        log = 0
        for i in tree:
            if i >= middle:
                log += i - middle
        if log < demand:
            end = middle -1
        elif log == demand:
            return middle
        else:
            start = middle + 1
        middle = (start+end)//2
    return middle
treeCnt, demand = map(int, input().split())
tree = list(map(int, input().split()))
answer = solution(demand, tree)
print(answer)