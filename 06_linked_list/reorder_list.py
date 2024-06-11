from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reorder_list(head: Optional[ListNode]) -> Optional[ListNode]:
    #0 -> n - 1 -> 1 -> n -2 ...
    #on step 2k + 1: from the end
    #on step 2k: from the start

    #get midpoint
    len = 0
    curr = mid =  head
    while curr:
        len += 1
        curr = curr.next
    midpoint = len // 2 #the right side will always be bigger

    for i in range(midpoint):
        mid = mid.next
    
    #reverse the latter half
    prev, mid_curr = None, mid
    while mid_curr:
        temp = mid_curr.next
        mid_curr.next = prev
        prev = mid_curr
        mid_curr = temp
    mid = prev

    #on odd steps, append the first half
    #on even steps, append the reversed latter half
    steps = 0
    res = curr = ListNode()
    while mid:
        if steps % 2 == 0 and steps // 2 < midpoint:
            curr.next = head
            head = head.next
        else:
            curr.next = mid
            mid = mid.next
        
        curr = curr.next
        steps += 1

    return res.next

def reorder_inplace(head: Optional[ListNode]) -> None:
    #fast and slow pointer method
    #slow pointer moves 1 step at a time, whereas fast moves 2
    #slow will end at the midpoint when fast arraives at the end
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    second = slow.next
    prev = slow.next = None #truncate the first half
    #reverse the second half of the list
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    
    first, second = head, prev

    #rearrange the array
    #zigzag pattern - Insert the second element between first's two elements
    #save both first.next and second.next as temps because we will be breaking them
    
    #using two pointers, second will always be shorter
    while second:
        tmp1, tmp2 = first.next, second.next
        #insert the second's element
        first.next = second
        #second's next pointer should point to first's next node
        second.next = tmp1
        #shift nodes
        first, second = tmp1, tmp2

def main():
    #head = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10, ListNode(12, None))))))
    #rearranged = reorder_list(head)
    #l = []
    #while rearranged:
    #    l.append(rearranged.val)
    #    rearranged = rearranged.next
    #print(l)

    head = ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10, ListNode(12, None))))))
    reorder_inplace(head)
    l = []
    while head:
        l.append(head.val)
        head = head.next
    print(l)

if __name__ == "__main__":
    main()