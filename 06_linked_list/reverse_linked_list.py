from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    #we need a temporary node to save current node's next pointer
    #the order of sequence is as follows

    #==Changing Current==#
    #1. store the pointer pointing to current's next node in a seperate pointer
    #2. change the current's next pointer to point to previous node

    #==Changing Next==#
    #3. current becomes previous
    #4. the current (now previous)'s next node will become current -> use the node info stored in step 1

    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    #at the end, the curr will be None
    #we need to return PREV!
    return prev

def main():
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, None))))
    reversed_list = reverse_list(head)
    l = []
    while reversed_list:
        l.append(reversed_list.val)
        reversed_list = reversed_list.next
    
    print(l)

if __name__ == "__main__":
    main()