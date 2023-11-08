def solution(n, m, section):
    answer = 0
    paint = section[0] - 1 # 페인트가 어디까지 왔는지
    for i in section:
        if i > paint:
            paint = i + m - 1
            answer += 1
    return answer