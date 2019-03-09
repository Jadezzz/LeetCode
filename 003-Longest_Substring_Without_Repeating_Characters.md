### 003 Longest Substring Without Repeating Characters

Medium

Given a string, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```



**Solution**

* [Sliding Window](http://www.csie.ntnu.edu.tw/~u91029/MaximumSubarray.html)



  A **sliding window** is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i,  j) [i, j)  (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i,  j) [i, j)  to the right by 1 element, then it becomes [i+1,  j+1) [i+1, j+1)  (left-closed, right-open).

  Back to our problem. We use HashSet to store the characters in current window [i,  j)  (j = i initially). Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i, we get our answer.



```Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        i = 0
        j = 0
        
        # Create an empty set
        char_set = set()
        
        while i < n and j < n:
            if(s[j] not in char_set):
                char_set.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                char_set.remove(s[i])
                i += 1
                
        return ans
```



