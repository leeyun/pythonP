class Solution:
    def GreedyP3(self, N, K):
        dev = 0
        sub = 0
        while N != 1:
            if N % K == 0:
                N //= K
                dev += 1
            else:
                N -= 1
                sub += 1
        if dev < sub:
            return dev
        else:
            return sub

N, K = map(int, input().split())
answer = Solution()
print(answer.GreedyP3(N, K))
