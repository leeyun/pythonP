class Solution:
    def ImplementationP4(self, matrix, x, y, direction, arr):
        # 0 1 2 3 시계방향
        # 북동남서
        # 북서남동
        answer = 1
        turntime = 0
        d = [[0]*matrix[0] for _ in range(matrix[1])]
        print(d)
        d[x][y] = 1
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while True:
            for _ in range(4):
                gotoX = x + dx[direction%3 + 1]
                gotoY = y + dy[direction%3 + 1]
                if arr[gotoX][gotoY] == 0 and d[gotoX][gotoY] == 0: # 안간곳인데 바다가 아닌 경우
                    x = gotoX
                    y = gotoY
                    direction = direction%3 + 1
                    turntime += 1
                    answer += 1
                    break
                if arr[gotoX][gotoY] == 1 or d[gotoX][gotoY] == 1: # 이미 간 곳 이거나 바다 인경우
                    direction = direction%3 + 1
                    turntime += 1
                # 돌기
            if turntime == 4:
                if direction == 0:
                    if arr[x + dx[2]][y + dy[2]] == 0:
                        answer += 1
                elif direction == 1: 
                    if arr[x + dx[2]][y + dy[2]] == 0:
                        answer += 1
                elif direction == 2: 
                    if arr[x + dx[2]][y + dy[2]] == 0:
                        answer += 1
                else: #서
                    if arr[x + dx[2]][y + dy[2]] == 0:
                        answer += 1
                break
            turntime = 0

        return answer

arr = []
matrix = list(map(int, input().split()))
x, y, direction = map(int, input().split())
for i in range(matrix[0]):
    arr.append(list(map(int, input().split())))
answer = Solution()
print(answer.ImplementationP4(matrix, x, y, direction, arr))