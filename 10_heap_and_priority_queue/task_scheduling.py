import heapq
from collections import deque
def leastInterval(tasks, n: int) -> int:
    #we need 3 things: 
    #count map
    #a max heap to keep track of remaining tasks
    #a double ended queue to keep track of tasks on idle

    #at point t, one of 3 things will happen:
    #1. from the task heap - do task and append to idle queue
    #2. if there's nothing in heap: bring task from queue to heap
    #3. if not time yet: idle

    taskCount = {}
    for t in tasks:
        taskCount[t] = taskCount.get(t, 0) + 1
      
    taskHeap = [-v for v in taskCount.values()]
    heapq.heapify(taskHeap)
    taskq = deque()
    #queue's elements will be a list
    #[-remaining task count, available time]

    t = 0
    while taskHeap or taskq: #either one can be empty
        
        t += 1
        if not taskHeap:
            t = taskq[0][1]
        else:
            remainingCount = heapq.heappop(taskHeap)
            if remainingCount + 1 != 0:
                #push back to queue if left
                taskq.append((remainingCount + 1, t + n))
        #bring task from idle queue to heap
        if taskq and taskq[0][1] == t:
            heapq.heappush(taskHeap, taskq.popleft()[0])
    
    return t

def main():
    tasks = ["X", "X", "Y", "Y"]
    n = 2
    a = leastInterval(tasks, n)
    print(a)
    test1 = [1, 2]
    test2 = []
    test1 += test2
    print(test1)

if __name__ == "__main__":
    main()