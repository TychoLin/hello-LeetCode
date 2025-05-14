class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        enum = list(enumerate(nums))

        def merge_sort(arr):
            mid = len(arr) // 2
            if mid:
                left = merge_sort(arr[:mid])
                right = merge_sort(arr[mid:])
                merged = []
                i = j = 0
                while i < len(left) or j < len(right):
                    if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                        result[left[i][0]] += j
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                return merged
            else:
                return arr

        merge_sort(enum)
        return result
