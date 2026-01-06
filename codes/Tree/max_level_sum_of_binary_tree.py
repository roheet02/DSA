# We use deque for efficient FIFO queue operations (O(1) pop from left)
from collections import deque
# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # value of current node
        self.left = left    # left child
        self.right = right  # right child

class Solution:
    def maxLevelSum(self, root):
        # Keeps track of current level number (root is level 1)
        curr_lvl = 1
        # Stores the maximum level sum seen so far
        maxi = float('-inf')
        # Stores the level number having maximum sum
        ans = 1
        # Queue for level order traversal (BFS)
        queue = deque([root])
        # BFS traversal of tree
        while queue:
            curr_sum = 0                # sum of values at current level
            lvl_size = len(queue)       # number of nodes at current level
            # Process all nodes of the current level
            for _ in range(lvl_size):
                node = queue.popleft()  # remove node from queue
                curr_sum += node.val   # add node value to level sum
                # Add left child to queue if exists
                if node.left:
                    queue.append(node.left)
                # Add right child to queue if exists
                if node.right:
                    queue.append(node.right)
            # Update maximum sum and level number if current level sum is greater
            if curr_sum > maxi:
                maxi = curr_sum
                ans = curr_lvl
            # Move to next level
            curr_lvl += 1
        # Return the level which has the maximum sum
        return ans
# Driver code
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
    print(sol.maxLevelSum(p))
