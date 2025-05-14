class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(root, p, q):
            if not root or root == p or root == q:
                return root

            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            if left and right:
                return root

            return left if left else right

        return helper(root, p, q)
