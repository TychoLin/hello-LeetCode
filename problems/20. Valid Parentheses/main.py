class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lefty = "([{"
        righty = ")]}"
        stack = []

        for c in s:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if not stack:
                    return False
                if righty.index(c) != lefty.index(stack.pop()):
                    return False

        return not stack
