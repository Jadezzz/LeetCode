### 001 Two Sum

Easy

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```Python
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```



**Solution:**

掃描兩次nums，第一次先將所有的數放在一個dict中，以數字為key，indice為value；第二次掃描nums，對於每一個數nums[i]，檢查target-nums[i]是否存在



```Python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
            # Numbers as key, indices as value
                keys[nums[i]] = i
```
