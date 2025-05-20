class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        used = [False] * len(nums)

        def helper():
            if len(path) == len(nums):
                result.append(list(path))
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    helper()
                    path.pop()
                    used[i] = False

        helper()
        return result
