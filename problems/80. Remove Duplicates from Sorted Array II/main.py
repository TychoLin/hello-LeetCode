class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeats = 2
        size = len(nums)

        if size <= repeats:
            return size

        k = repeats
        for i in range(repeats, size):
            if nums[i] != nums[k - repeats]:
                nums[k] = nums[i]
                k += 1
        return k
