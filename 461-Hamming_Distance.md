### 461 Hamming Distance

Easy

The [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) between two integers is the number of positions at which the corresponding bits are different.

Given two integers `x` and `y`, calculate the Hamming distance.

**Note:**
0 ≤ `x`, `y` < 2^31.

**Example:**

```
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```



**Solution**

用bitwise操作，兩個數做exclusive or得到c，不同的地方就會留下1，再去計算c的bit中，1的個數，即可得到Hamming Distance

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        c = x ^ y
        for i in range(32):
            if c & 1 == True:
                count += 1
            c = c >> 1
        
        return count
```

