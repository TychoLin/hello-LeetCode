class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search_first(nums, target):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                if target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            if low < len(nums) and target == nums[low]:
                return low
            else:
                return -1

        def search_last(nums, target):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                if target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            if low - 1 >= 0 and target == nums[low - 1]:
                return low - 1
            else:
                return -1

        return [search_first(nums, target), search_last(nums, target)]
