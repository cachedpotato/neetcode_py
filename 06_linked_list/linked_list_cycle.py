from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def is_cyclic(head: Optional[ListNode]) -> bool:
    #yet another fast and slow pointer approach
    #if there is a cycle, there will be a point
    #where slow and fast overlaps
    #if not, the fast will reach None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False