class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def get_height(node, go_left):
            height = 0
            while node:
                node = node.left if go_left else node.right
                height += 1
            return height

        left_height = get_height(root, True)
        right_height = get_height(root, False)

        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
