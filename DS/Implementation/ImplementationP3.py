class Solution:
    def ImplementationP3(self, location):
        cnt = 0
        move = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (2, -1)]
        tmp1 = ord(location[0]) - ord('a')
        tmp2 = int(location[1]) - 1
        for m in move:
            loc1 = tmp1 + m[0]
            loc2 = tmp2 + m[1]
            if loc1 > 0 and loc1 < 8 and loc2 > 0 and loc2 < 8:
                cnt += 1
        
        return cnt
                        
location = input()
answer = Solution()
print(answer.ImplementationP3(location))