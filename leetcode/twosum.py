class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = []
        for i in range(len(nums)):
             for j in range(i + 1, len(nums)):
                 if nums[i] + nums[j] == target:
                     answer = i, j
                     return answer

nums = [3,2,4]
target = 6
answer = Solution()
print(answer.twoSum(nums, target))