class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def helper(remaining, start, combinations):
            if remaining == 0:
                result.append(list(combinations))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                combinations.append(candidates[i])
                helper(remaining - candidates[i], i, combinations)
                combinations.pop()

        helper(target, 0, [])
        return result
