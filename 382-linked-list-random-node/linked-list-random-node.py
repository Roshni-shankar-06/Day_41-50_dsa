import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        res = self.head.val
        curr = self.head.next
        i = 2
        
        while curr:
            # random.randint(1, i) includes both endpoints
            if random.randint(1, i) == 1:
                res = curr.val
            curr = curr.next
            i += 1
            
        return res
