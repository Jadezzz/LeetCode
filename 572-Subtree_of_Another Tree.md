###572 Subtree of Another Tree

Easy

Given two non-empty binary trees **s** and **t**, check whether tree **t** has exactly the same structure and node values with a subtree of **s**. A subtree of **s** is a tree consists of a node in **s**and all of this node's descendants. The tree **s** could also be considered as a subtree of itself.

**Example 1:**
Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
```

Given tree t:

```
   4 
  / \
 1   2
```

Return ```true```

because t has the same structure and node values with a subtree of s.



**Example 2:**
Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```

Given tree t:

```
   4
  / \
 1   2
```

Return ```false```



### Solution

1. Preorder traverse the binary tree so that

   ``` 
            4
          /   \  
         /      \
       1          2
      /  \       /  \
    lnull rnull lnull rnull
   ```

   truns into string "#4 #1 lnull rnull #2 lnull rnull"

2. compare two strings, check if t tree is the substring of s tree

   (Using the str1.find(str2) function, return -1 if not found, return start index if found)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def preorder(t, left):
            if t == None:
                if left:
                    return 'lnull'
                else:
                    return 'rnull'
            return ('#' + str(t.val) + ' ' + 
                    preorder(t.left, True) + ' ' + 
                    preorder(t.right, False))
        
        tree1 = preorder(s, True)
        tree2 = preorder(t, True)
        
        return True if tree1.find(tree2) >= 0 else False
        
```

