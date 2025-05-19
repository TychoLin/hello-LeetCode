class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])
                bit = 1 << val
                box_index = (i // 3) * 3 + (j // 3)

                if rows[i] & bit or cols[j] & bit or boxes[box_index] & bit:
                    return False

                rows[i] |= bit
                cols[j] |= bit
                boxes[box_index] |= bit

        return True
