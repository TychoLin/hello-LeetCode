class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first

                top = matrix[first][i]
                matrix[first][i] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top
