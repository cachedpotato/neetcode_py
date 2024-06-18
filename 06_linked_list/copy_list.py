from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node', random: 'Node') -> None:
        self.val = x
        self.next = next
        self.random = random

def copy_list(head: 'Optional[Node]') -> 'Optional[Node]': 
    #randoms point to literally anywhere, how do we connect this without making a mess?
    #answer? HASHMAPS!
    #Hashmap with key (origina) and value (copy nodes)
    #in first loop: just add the value info and store in has
    #second loop: add connections, both next and random, via searching through hashmap

    #IF WE WANT TO REARRANGE SOMETHING THAT IS ENTANGLED, OR CONNECTED IN SOME CONVOLUTED WAY,
    #THINK OF HASHMAPS AND ADDING CONNECTIONS THROGH SEARCHING


    nodes = {None:None} #for None handling: insert None:None before anything
    curr = head

    #STEP1. ADDING VALUES ONLY THEN UPDATING HASHMAP
    while curr:
        new_node = Node(x = curr.val)
        nodes[curr] = new_node
        curr = curr.next
    
    #STEP2. ADDING CONNECTIONS
    curr = head
    while curr:
        #next info
        curr_copy = nodes[curr]
        curr_copy.next = nodes[curr.next]
        curr_copy.random = nodes[curr.random]

        curr = curr.next
    
    return nodes[head]
    