class Twitter:

    def __init__(self):
        self.tweets = {} #user:tweets[(time, id)]
        self.followers = {} #user:followers[]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = [(self.time, tweetId)]
        else:
            self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        people = {userId}
        if userId in self.followers:
            for i in self.followers[userId]:
                people.add(i)

        for p in people:
            if p in self.tweets:
                idx = len(self.tweets[p]) - 1
                time, tweetId = self.tweets[p][idx]
                heapq.heappush(heap, ((-1)*time, tweetId, p, idx))

        ans = []
        while heap and len(ans) < 10:
            time, tweetId, p, idx = heapq.heappop(heap)
            ans.append(tweetId)
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[p][idx]
                heapq.heappush(heap, ((-1)*time, tweetId, p, idx))

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.followers:
            self.followers[followerId] = {followeeId}
        else:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers or followeeId not in self.followers[followerId]: return
        self.followers[followerId].remove(followeeId)
        
