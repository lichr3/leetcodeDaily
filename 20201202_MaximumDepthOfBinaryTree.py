# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root != None:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0

    def maxDepth2(self, root: TreeNode) -> int:
        nodes = [root]
        while len(nodes) > 0:
            tmp = nodes[0]
            if tmp.left is not None:
                nodes

root = TreeNode(val = 0, left = TreeNode(), right = TreeNode())
test = Solution()
print(test.maxDepth(root))