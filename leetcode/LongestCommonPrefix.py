class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ""
        flag = True
        minStr = min(strs, key = len)
        for i, value in enumerate(minStr):
            for word in strs:
                if value == word[i]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                answer += value
            else:
                break
        return answer
            
strs = ["flower", "flow", "flight"]
answer = Solution()
print(answer.longestCommonPrefix(strs))