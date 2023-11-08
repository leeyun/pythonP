def solution(state, budget):
    start = 1
    end = max(state)
    middle = (start + end) // 2
    while start <= end:
        divide = 0
        for i in state:
            if i >= middle:
                divide += middle
            else:
                divide += i
        if divide < budget:
            start = middle + 1
        elif divide == budget:
            return middle
        else:
            end = middle - 1
        middle = (start + end) // 2
    return middle

N = int(input())
state = list(map(int, input().split()))
budget = int(input())
answer = solution(state, budget)
print(answer)