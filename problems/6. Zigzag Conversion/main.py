class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        results = [''] * numRows
        row = 0
        change_direction = False

        for c in s:
            results[row] += c
            if row == 0 or row == numRows - 1:
                change_direction = not change_direction
            row += 1 if change_direction else -1

        return ''.join(results)
