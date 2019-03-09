### 581 Shortest Unsorted Continuous Subarray

Easy

Given an integer array, you need to find one **continuous subarray** that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the **shortest** such subarray and output its length.

**Example 1:**

```
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
```



**Note:**

1. Then length of the input array is in range [1, 10,000].
2. The input array may contain duplicates, so ascending order here means **<=**.



**Solution 1**

1. Sort the array
2. Compare each element in two arrays
3. record the index of the left most and right most different element

Time Complexity: O(nlogn)  for sorting

Space Complexity: O(n)

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = sorted(nums)
        left_min = len(nums)
        right_max = 0
        for i, num in enumerate(nums):
            if(num != nums_copy[i]):
                left_min = min(left_min, i)
                right_max = max(right_max, i)
                
        if left_min == len(nums) or right_max == 0 :
            return 0
        else:   
            return right_max - left_min + 1
```



**Solution 2**

We use three loops:

1. traverse array from beginning, find the minimum element in the unsorted part
2. traverse array backwards, find the maximum element in the unsorted part
3. search forward, find index just larger than the minimum element, which is the left bound
4. search backward, find index just smaller than the maximum element, which is the right bound 

![](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/Figures/581/Unsorted_subarray_2.PNG)

```python
import sys

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        minimum = sys.maxsize
        maximum = -sys.maxsize
        
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                minimum = min(minimum, nums[i])
        
        for i in reversed(range(n -1)):
            if nums[i] > nums[i+1]:
                maximum = max(maximum, nums[i])
        
        left_bound = 0
        right_bound = n-1
        
        for i in range(n):
            if minimum < nums[i]:
                break
            else:
                left_bound += 1
        
        for i in reversed(range(n)):
            if maximum > nums[i]:
                break
            else:
                right_bound -= 1
                
        return 0 if right_bound - left_bound < 0 else right_bound - left_bound + 1
```

