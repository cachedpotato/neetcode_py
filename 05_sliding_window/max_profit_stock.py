def max_profit(prices) -> int:
    res = 0
    #buy high, sell low
    #constraint: we can't go back in time and sell, so
    #profit will always take the form of prices[r] - prices[l]
    l = r = 0
    while r < len(prices):
        #we will be looking at the perspective of MINIMUM PRICE (l)
        #keep moving r down the list
        #if we get a value smaller than the current l,
        #jump l to that value
        #no need for checking back all the way to r because we've already done so
        #by moving r
        if prices[l] <= prices[r]:
            res = max(res, prices[r] - prices[l])
        else:
            #new minimum found
            #jump l to current r
            l = r
        
        r += 1

    return res

def main():
    prices = [10, 1, 5, 6, 7, 1]
    print("max profit: {}".format(max_profit(prices)))

if __name__ == "__main__":
    main()