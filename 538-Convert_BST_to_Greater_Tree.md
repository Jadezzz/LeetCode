### 538 Convert BST to Greater Tree

Easy

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

**Example:**

```
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
```



#### Solution

Since the origin tree is a binary search tree, val in the right subtree is always bigger than the value and value in the left subtree.

Use a stack to traverse the binary search tree from the largest value. Keep a sum to track the value visited.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum = 0
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            sum += node.val
            node.val = sum
            
            node = node.left
        
        return root
```

