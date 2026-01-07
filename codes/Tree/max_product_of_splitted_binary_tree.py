# definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root):
        
        # modulo is needed because product can get very large
        MOD = 10**9 + 7
        
        # this will store the maximum product we find
        self.best = 0
        
        # first, calculate the total sum of the entire tree
        def total_sum(node):
            # if node is none, contribution is zero
            if not node:
                return 0
            
            # sum = current node value + left subtree + right subtree
            return node.val + total_sum(node.left) + total_sum(node.right)
        
        # total sum of all nodes in the tree
        total = total_sum(root)
        
        # now do dfs again to calculate subtree sums
        # and try splitting the tree at every possible node
        def dfs(node):
            # base case
            if not node:
                return 0
            
            # sum of subtree rooted at current node
            s = node.val + dfs(node.left) + dfs(node.right)
            
            # imagine cutting the edge above this subtree
            # one part has sum = s
            # the other part has sum = total - s
            # update the best product
            self.best = max(self.best, s * (total - s))
            
            # return subtree sum so parent can use it
            return s
        
        # start dfs traversal from root
        dfs(root)
        
        # return the final answer with modulo
        return self.best % MOD

if __name__ == "__main__":
    # Constructing binary tree:
    #          1
    #        /   \
    #       2     2
    #      / \   / \
    #     3   4 4   3
    p = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3))
    )
    sol = Solution()
    print(sol.maxProduct(p))