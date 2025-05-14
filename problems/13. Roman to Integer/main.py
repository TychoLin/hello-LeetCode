class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {}
        romans["I"] = 1
        romans["V"] = 5
        romans["X"] = 10
        romans["L"] = 50
        romans["C"] = 100
        romans["D"] = 500
        romans["M"] = 1000

        total = 0
        fast = 1

        while fast < len(s):
            slow = fast - 1
            if romans[s[fast]] <= romans[s[slow]]:
                total += romans[s[slow]]
            else:
                total -= romans[s[slow]]
            fast += 1
        total += romans[s[-1]]

        return total
