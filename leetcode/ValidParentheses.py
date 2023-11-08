class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif i == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif i == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        return True
s = "()[]{}"
answer = Solution()
print(answer.isValid(s))