"""
    Unit23 [2차원 리스트]
    1. 리스트 2차원 표현식
    + 변수1 = [[변수2 for j in range(반복)]for i in range(반복)]

    2. 2차원 리스트의 할당과 복사
    + 변수 = copy.deepcopy(객체)
        변수1 = 변수2나 변수1 = 변수2.copy()는 같은 요소를 공유한다(2차원만 해당)
"""
# 연습문제: 3차원 리스트 만들기
a = [[[0 for k in range(3)]for j in range(4)]for i in range(2)]
print(a)

# 심사문제: 지뢰찾기
col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
location = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            print('*', end = '')
        else:
            count = 0
            for updown, leftright in location:
                if i + updown < 0 or i + updown >= row:
                    continue
                elif j + leftright < 0 or j + leftright >= row:
                    continue
                elif matrix[i + updown][j + leftright] == '*':
                    count += 1
            print(count, end = '')
    print()
