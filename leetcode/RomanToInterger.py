class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        answer = 0
        Symbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while index != len(s):
            if index + 2 <= len(s) and Symbol[s[index]] < Symbol[s[index + 1]]:
                answer += Symbol[s[index + 1]] - Symbol[s[index]]
                index += 2
            else:
                answer += Symbol[s[index]]
                index += 1
        return answer

s = "MCMXCIV"
answer = Solution()
print(answer.romanToInt(s))
