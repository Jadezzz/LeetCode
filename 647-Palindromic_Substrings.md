### 647 Palindromic Substrings

Medium

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

**Example 1:**

```
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

 

**Example 2:**

```
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

 

**Note:**

1. The input string length won't exceed 1000.



**Solution**

* 每一個字母單獨都算palindrome
* 以一個字母center的palindrome，測試左邊右邊是不是相等，相等+1
* 以兩個字母center的palindrome，測試左邊右邊是不是相等，相等+1

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            # Every char is a new palindromic string
            ans += 1
            
            # Odd Number centered
            left = i - 1
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1
                    ans += 1
            
            # Even Number centered
            left = i
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1
                    ans += 1
                    
        return ans
```

