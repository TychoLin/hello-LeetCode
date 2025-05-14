class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        results = [[] for i in range(numRows)]
        row = 0
        diff = 1
        for c in s:
            row = min(row, numRows - 1)
            results[row].append(c)
            if row == numRows - 1:
                diff = -1
            if row == 0:
                diff = 1
            row += diff
        return "".join(("".join(word) for word in results))
