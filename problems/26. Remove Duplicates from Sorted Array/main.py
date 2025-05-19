class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
