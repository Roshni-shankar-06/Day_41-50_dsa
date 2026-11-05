class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        
        # 1. Push all nodes of l1 onto stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        # 2. Push all nodes of l2 onto stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        head = None
        
        # 3. Pop elements and add them up from right to left
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node and link it to the front of our result list
            node = ListNode(total % 10)
            node.next = head
            head = node
            
        return head
