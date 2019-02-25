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
                
                