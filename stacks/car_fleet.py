def car_fleet(target, position, speed) -> int:
    res = 0

    #how does a fleet occur?
    #fleet occurs when the car behind is 1) faster,
    #and 2) will have intersected BEFORE (or at) the destination
    car_zip = zip(position, speed)
    current_time = 0

    for p, s in sorted(car_zip, reverse = True):
        time_till_destination = (target - p)/s
        if time_till_destination > current_time:
            #we're thinking in REVERSE
            #this if block is accessed iff the car at the back
            #is NOT able to catch up, thereby
            #creating its own fleet
            res += 1
            current_time = time_till_destination
    
    return res

def main():
    target = 10
    position = [4,1,0,7]
    speed = [2,2,1,1]

    print(car_fleet(target, position, speed))



if __name__ == "__main__":
    main()

