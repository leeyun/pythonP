def solution(braket):
    answer = 0
    temp = 1
    stack = []
    for i in range(len(braket)):
        word = braket[i]
        if word == "(":
            stack.append(word)
            temp *= 2
        elif word == "[":
            stack.append(braket[i])
            temp *= 3
        elif word == ")":
            if not stack or stack[-1] == "[":
                return 0
            if braket[i - 1] == "(":
                answer += temp
            temp //= 2
            stack.pop()
        else:
            if not stack or stack[-1] == "(":
                return 0
            if braket[i - 1] == "[":
                answer += temp
            temp //= 3
            stack.pop()
    if stack:
        return 0
    return answer
braket = input()
print(solution(braket))