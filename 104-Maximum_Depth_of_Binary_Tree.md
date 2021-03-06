### 104 Maximum Depth of Binary Tree

Easy

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Note:** A leaf is a node with no children.

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its depth = 3.



#### Solution

Use recursion

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def bfs(t, level):
            if t == None:
                return 0
            
            left = t.left
            right = t.right
            
            return 1 + max(bfs(left, level+1), bfs(right, level+1))
        
        return bfs(root, 1)
```

