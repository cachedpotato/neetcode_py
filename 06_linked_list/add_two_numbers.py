from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummy = res = ListNode()
    while l1 and l2:
        s = l1.val + l2.val + carry
        carry = 0
        if s > 9:
            carry = 1
            s -= 10
        dummy.next = ListNode(val = s)
        dummy = dummy.next
        l1 = l1.next
        l2 = l2.next
    
    dummy.next = l1 or l2
    
    while carry == 1:
        if dummy.next == None:
            dummy.next = ListNode(1, None)
            return res.next
        
        else:
            s = dummy.next.val + carry
            carry = 0
            if s > 9:
                carry = 1
                s = s - 10
            dummy.next.val = s
            dummy = dummy.next
    
    return res.next

def main():
    l1 = ListNode(9, None)
    l2 = ListNode(9, None)
    v = []
    s = addTwoNumbers(l1, l2)
    while s:
        v.append(s.val)
        s = s.next
    print(v)

if __name__ == "__main__":
    main()