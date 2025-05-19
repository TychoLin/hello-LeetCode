class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] != val:
                nums[k] = nums[cur]
                k += 1
            cur += 1
        return k
