### 560 Subarray Sum Equals K

Medium

Given an array of integers and an integer **k**, you need to find the total number of continuous subarrays whose sum equals to **k**.

**Example 1:**

```
Input:nums = [1,1,1], k = 2
Output: 2
```



**Note:**

1. The length of the array is in range [1, 20,000].
2. The range of numbers in the array is [-1000, 1000] and the range of the integer **k** is [-1e7, 1e7].

#### Solution

Use a hashmap ```(sum, # of occurance of sum)``` to store cummulative sum

Also, compute ```sum-k``` , check if this value exsist in the dict ```(sum-k, # of sum-k)``` , if this value exists, we have found ``` # of sum-k ``` sections that can fullfill the need

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        summ = 0
        d = collections.defaultdict(int)
        d[0] = 1
        result = 0
        for i in range(n):
            summ += nums[i]
            if summ-k in d:
                result += d[summ-k]
            d[summ] += 1
        
        return result
```

