from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #at any given point - compare current list's next node and other list's current node
    #if other list is bigger > append that node, and current list becomes the other list
    #if the list reaches the end: append whatever's left of the other list, then return

    #I used copies of lists before, can we reduce the number of copies,
    # or better yet, not use temp list at all?

    #quick edge case returns
    if list1 and not list2: return list1
    if list2 and not list1: return list2
    if not list1 and not list2: return None


    #step 1: initialization - which list do we start off with?
    #create a Dummy so that list1 is always the starting list
    #when we return, just return the next pointer
    if list1.val > list2.val:
        temp = list1
        list1 = list2
        list2 = temp
    
    dummy = ListNode(0, list1)
    while list1:
        #step 2: comparison
        #between current list's next value and other list's current value
        if list1.next and list1.next.val > list2.val:
            #swap lists
            temp = list1.next
            list1.next = list2
            list2 = temp
    
        #step 3: check if there's any remaining nodes
        if not list1.next and list2:
            list1.next = list2
            return dummy.next

        list1 = list1.next
    
    return dummy.next

def merge_two_sorted_list_optimized(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #Okay I may be a bit dumb
    #create a separate node (a third node list)
    #that starts at some random value, then appends list1 and list2
    #this will CONSUME the leftmost node of a given list (list = list.next)
    #have another node that points to the starting point of this new third list and return that

    #may seem unintuitive but both dummy and node is
    #pointing to the SAME address!
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val <= list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        
        node = node.next
    
    #there may be some list nodes left
    #append that to node's next
    node.next = list1 or list2 #either one of the two is Some and the other None

    return dummy.next

def main():
    list1 = ListNode(1, ListNode(2, ListNode(4, None)))
    list2 = ListNode(1, ListNode(3, ListNode(6, None)))

    merged_list = merge_two_sorted_lists(list1, list2)
    l = []
    while merged_list:
        l.append(merged_list.val)
        merged_list = merged_list.next
    
    print(l)


    list1 = ListNode(1, ListNode(2, ListNode(4, None)))
    list2 = ListNode(1, ListNode(3, ListNode(6, None)))
    merged_list = merge_two_sorted_list_optimized(list1, list2)
    l = []
    while merged_list:
        l.append(merged_list.val)
        merged_list = merged_list.next
    
    print(l)

if __name__ == "__main__":
    main()