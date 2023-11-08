class Solution:
    # N: 배열의 크기, M: 더할 수 있는 횟수, K: 동일 인덱스 수 가능 횟수
    def GreedyP1(self, L, N, M, K):
        answer = 0
        L.sort(reverse = True)
        cnt = K
        for _ in range(M):
            if cnt != 0:
                answer += L[0]
                cnt -= 1
            else:
                answer += L[1]
                cnt = K
        return answer
    
    def GreedyP1_Optimization(self, L, N, M, K):
        L.sort(reverse = True)
        count = int(M/(K+1) * K) # 가장 큰수가 나오는 횟수
        count += M%(K+1) # 나누어 떨어지지 않을 경우 나오는 큰 수 횟수

        answer = 0
        answer += (count) * L[0]
        answer += (M - count) * L[1] # 작은 수가 나오는 횟수 * 작은수

        return answer
answer = Solution()
N, M, K = map(int, input().split())
L = list(map(int, input().split()))
print(answer.GreedyP1(L, N, M, K))
print(answer.GreedyP1_Optimization(L, N, M, K))

