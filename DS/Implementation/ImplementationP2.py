class Solution:
    def ImplementationP2(self, hour):
        cnt = 0
        for h in range(hour+1):
            for m in range(60):
                for s in range(60):
                    if '3' in str(h) + str(m) + str(s):
                        cnt += 1
        return cnt
    
hour = int(input())
answer = Solution()
print(answer.ImplementationP2(hour))