class TimeMap:
    #because set is always done in a sequential manner
    #every data stored will be sorted
    #can we use this to optimize our class?
    def __init__(self) -> None:
        #key value pair
        #key(name) : [(time, value), (time, value), ...]
        self.keys = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.keys.get(key) == None:
            self.keys[key] = []
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #Binary Search for timestamp value
        #closest to timestamp given (but has to be bigger or equal):
        res = 1001
        if self.keys.get(key) == None or self.keys[key][0][0] > timestamp: return ""
        if timestamp > self.keys[key][-1][0]: return self.keys[key][-1][1]
        l = 0
        r = len(self.keys[key]) - 1
        while l <= r:
            split = l + (r - l) // 2
            curr = self.keys[key][split]
            if curr[0] == timestamp:
                return curr[1]
            elif curr[0] < timestamp:
                if timestamp < self.keys[key][split + 1][0]:
                    return curr[1]
                #small
                #update
                res = curr[0]
                l = split + 1
            else:
                r = split - 1
    
    def get_cleaner(self, key: str, timestamp: int) -> str:
        res, value = "", self.keys.get(key, []) #did not know I can initialize stuff like this
        l, r = 0, len(value) - 1

        #remember, BSA is robust in that it won't return error
        #even if we don't find the value in the list
        #set the default result value to something then just do the BSA
        while l <= r:
            split = l + (r - l) // 2
            if value[split][0] == timestamp:
                return value[split][1]
            elif value[split][0] < timestamp:
                #we are behind the timestamp
                #it may be the answer, it may be not
                #update res
                res = value[split][1]
                l = split + 1
            else:
                #we are after the timestamp
                #this CANNOT be the answer
                r = split - 1
        
        return res

        
def main():
    timeMap = TimeMap()
    timeMap.set("alice", "happy", 1)
    v1 = timeMap.get("alice", 1)
    print(v1)
    v2 = timeMap.get("alice", 2)
    print(v2)
    timeMap.set("alice", "sad", 3)
    v3 = timeMap.get("alice", 3)     
    print(v3)
    timeMap.set("alice", "anxious", 7)
    v4 = timeMap.get_cleaner("alice", 6)
    print(v4)
    print(timeMap.get("alice", 7))
    print(timeMap.get("Rose", 0))

if __name__ == "__main__":
    main()

            