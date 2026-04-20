class Twitter:

    def __init__(self):
        self.tweets = {} #user:tweets[(time, id)]
        self.followers = {} #user:followers[]
        self.time = 0
        self.heap = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = [(self.time, tweetId)]
        else:
            self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        newTweets = [t for t in self.tweets[userId]] if userId in self.tweets else []
        if userId in self.followers:
            for follower in self.followers[userId]:
                if follower in self.tweets:
                    newTweets.extend([t for t in self.tweets[follower]])

        print([i[1] for i in newTweets])
        return [i[1] for i in sorted(newTweets, key=lambda x:x[0], reverse=True)][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.followers:
            self.followers[followerId] = {followeeId}
        else:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers or followeeId not in self.followers[followerId]: return
        self.followers[followerId].remove(followeeId)
        
