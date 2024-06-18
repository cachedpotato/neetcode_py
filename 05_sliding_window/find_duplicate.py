def find_duplicate(nums) -> int:
    #floyd's algorithm
    #because the length of nums is n + 1 and the range of the values are [1, n]:
    #we can view the list as a LINKED LIST where:
    #node i points to node nums[i]
    #AKA every nums[i] "operation" is a jump to the next connected node
    #and 2: index 0 is always the "starting point" of the linked list, because
    #the values are between 1 and n.
    
    #there is exactly ONE duplicate, meaning
    #there exists just ONE node where two nodes point to it
    #this creates a CYCLE of an arbitrary size but will NEVER include node 0.
    
    #floyd's algorithm consists of two phases:
    #PHASE1: INTERSECTION ACQUISITION
    #using the fast and slow pointer method, we must get an intersection point
    
    #PHASE2: DUPLICATION ACQUISITION
    #have two pointers, one at node 0 and one at the intersection node we found at phase 1
    #keep moving pointers one by one untill we intersect again.
    #this intersection will be the START of the cycle, and will be the answer


    #phase 1
    fast = slow = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast: break
    
    #phase 2
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2: return slow

def main():
    test1 = [1, 1, 2, 3]
    test2 = [1, 2, 3, 4, 4]
    test3 = [1, 6, 2, 5, 3, 4, 6]
    test4 = [5, 2, 1, 3, 5, 4]
    for test in [test1, test2, test3, test4]:
        print(find_duplicate(test))

if __name__ == "__main__":
    main()