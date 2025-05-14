class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        table = {}

        for i, num in enumerate(sorted_nums):
            if num not in table:
                table[num] = i

        return [table[num] for num in nums]
