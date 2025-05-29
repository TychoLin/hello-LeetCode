class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = [False] * len(arr)

        def helper(start):
            if start >= len(arr) or start < 0 or visited[start]:
                return False
            if arr[start] == 0:
                return True

            visited[start] = True

            return helper(start + arr[start]) or helper(start - arr[start])

        return helper(start)


class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = [False] * n
        queue = deque([start])
        visited[start] = True

        while queue:
            i = queue.popleft()

            if arr[i] == 0:
                return True

            for next_i in [i + arr[i], i - arr[i]]:
                if 0 <= next_i < n and not visited[next_i]:
                    visited[next_i] = True
                    queue.append(next_i)

        return False
