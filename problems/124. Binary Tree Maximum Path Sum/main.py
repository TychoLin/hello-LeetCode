class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')

        def helper(root):
            if not root:
                return 0

            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)

            path_sum = root.val + left + right
            self.max_sum = max(self.max_sum, path_sum)

            return root.val + max(left, right)

        helper(root)
        return self.max_sum
