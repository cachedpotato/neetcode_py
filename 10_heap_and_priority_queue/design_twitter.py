import heapq
class Twitter:
  def __init__(self) -> None:
    #key: user -> value: [set(followerId), [minHeap of posts]]
    self.user = {}

  def postTweet(self, userId: int, tweetId: int) -> None:
    if not self.user.get(userId):
      self.user[userId] = [set(), []]
    
    #root is smallest > oldeest
    heapq.heappush(self.user[userId][1], tweetId)
    #remove oldest posts
    while len(self.user[userId][1]) > 10:
      heapq.heappop(self.user[userId][1])
  
  def getNewsFeed(self, userId: int):
    #get news of self and followers
    #post 10 MOST RECENT (bigger ID)
    #we need maxHeap for popping

    #check if user exists
    if not self.user.get(userId):
      return []
    
    totalNewsFeed = self.user[userId][1].copy()
    for followerId in self.user[userId][0]:
      totalNewsFeed +=  self.user[followerId][1].copy()
    
    #convert to maxHeap
    totalNewsFeed = [-id for id in totalNewsFeed]
    heapq.heapify(totalNewsFeed)

    res = []
    for _ in range(10):
      if len(totalNewsFeed) == 0:
        break

      res.append( -1 * heapq.heappop(totalNewsFeed)) 
    return res
  
  def follow(self, followerId: int, followeeId: int) -> None:
    for f in [followerId, followeeId]:
      if not self.user.get(f):
        self.user[f] = [set(), []]
    
    self.user[followerId][0].add(followeeId)
  
  def unfollow(self, followerId: int, followeeId: int) -> None:
    for f in [followerId, followeeId]:
      if not self.user.get(f):
        self.user[f] = [set(), []]

    if followeeId in self.user[followerId][0]:
      self.user[followerId][0].remove(followeeId)




    