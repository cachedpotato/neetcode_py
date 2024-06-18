from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #my highly inefficient approach
    #reverse the list first
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr= temp

    reverse = dummy = prev
    #reach the nth position from the back
    #edge case: n = 1
    if n == 1:
        dummy = dummy.next
    else:
        i = 1
        while i < n - 1:
            reverse = reverse.next
            i += 1
        
        #skip next
        #edge case: there is no next
        #n == len(head)
        #just skip the first value of head and return
        if not reverse.next.next:
            return head.next
        reverse.next = reverse.next.next
    
    #re-reverse
    prev, curr = None, dummy
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def remove_nth_from_end_optimized(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #instead of reversing 2 times, we can just use 2 pointers of gap n
    #ex)l points to node 0 and r points to node n - 1
    #once we keep going down the list, and r reaches null, l will be
    #at the EXACT position where the node we want to skip is placed
    #that means we need access to the node previous to l - how do we do this?
    #we can add a dummy node BEFORE the first node, and initialize l there, and r remains the same
    #ex) n = 3
    #DUMMY(L) - NODE0 - NODE1 - NODE2 - NODE3*(r) - NODE4 - NODE5 
    #DUMMY - NODE0 - NODE2(l) - NODE3* - NODE4 - NODE5 - NULL(r)
    l = dummy = ListNode(0, head)
    r = head

    for i in range(n):
        r = r.next
    
    #move both pointers till r reaches None
    while r:
        l = l.next
        r = r.next

    #remove node
    l.next = l.next.next

    return dummy.next

def main():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))
    n = 2
    skipped = remove_nth_from_end_optimized(head, n)
    v = []
    while skipped:
        v.append(skipped.val)
        skipped = skipped.next
    print(v)

if __name__ == "__main__":
    main()