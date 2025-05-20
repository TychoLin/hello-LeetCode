class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        end = 0
        farthest = 0
        jumps = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                end = farthest
                jumps += 1
                if end >= (n - 1):
                    break

        return jumps
