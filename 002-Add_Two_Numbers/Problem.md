### 002 Add Two Numbers

Medium

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```



**注意測資有\[0][0]**



**Solution1:**

(First Time)

先求和，再一位一位的建立linked list

```Python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        i = 1
        while True:
            num1 += l1.val*i
            if l1.next == None:
                break
            else:
                l1 = l1.next
                i *= 10
        
        num2 = 0
        i = 1
        while True:
            num2 += l2.val*i
            if l2.next == None:
                break
            else:
                l2 = l2.next
                i *= 10
        
        num = num1 + num2
        
        # Handle Edge Case
        if num == 0:
            return ListNode(0)

        head = None
        cur = None
        while num > 0:
            if head == None:
                head = ListNode(num % 10)
                num //= 10
                cur = head
            else:
                nextt = ListNode(num % 10)
                num //= 10
                cur.next = nextt
                cur = nextt
        
        return head
```



