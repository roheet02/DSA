# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return 0,None
            left_h,left_node=dfs(node.left)
            right_h,right_node=dfs(node.right)
            if left_h>right_h:
                return left_h+1,left_node
            elif right_h>left_h:
                return right_h+1,right_node
            else:
                return left_h+1,node
        return dfs(root)[1]

if __name__ == "__main__":
    # Constructing binary tree:
    #          1
    #        /   \
    #       2     2
    #      / \   / \
    #     3   4 4   3
    p = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4, TreeNode(5), None)),
        TreeNode(2, TreeNode(4), TreeNode(3))
    )
    sol = Solution()
    print(sol.subtreeWithAllDeepest(p))
    ans = sol.subtreeWithAllDeepest(p)
    print(ans.val if ans else None)