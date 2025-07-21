class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split('/')
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        cur = 1
        walker = 1
        stack = []

        while walker < len(path):
            while walker < len(path) and path[walker] == '/':
                walker += 1
            cur = walker

            while walker < len(path) and path[walker] != '/':
                walker += 1

            part = path[cur:walker]
            if part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path[cur:walker])
            cur = walker

            while walker < len(path) and path[walker] == '/':
                walker += 1
            cur = walker

        return "/{}".format('/'.join(stack))
