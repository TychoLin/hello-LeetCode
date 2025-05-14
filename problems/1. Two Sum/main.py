class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, value in enumerate(nums):
            if target - value in table:
                return (i, table[target - value])
            table[value] = i


nums = [2, 7, 11, 15]
target = 9
result = Solution().twoSum(nums, target)
