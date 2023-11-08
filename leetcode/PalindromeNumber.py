class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            reverse = 0
            origin = x
            while origin:
                remainder = origin % 10
                origin = origin//10
                reverse = reverse*10 + remainder
            if reverse == x:
                return True
            else:
                return False
x = 121
answer = Solution()
print(answer.isPalindrome(x))
        