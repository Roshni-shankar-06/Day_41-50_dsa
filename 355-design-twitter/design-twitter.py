from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0  # Global timestamp
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1  # Decrement to use min-heap as max-heap

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []
        
        # Ensure user follows themselves to see their own tweets
        self.followMap[userId].add(userId)
        
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
                
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop(minHeap)
            res.append(tweetId)
            if nextIndex >= 0:
                prevCount, prevTweetId = self.tweetMap[followeeId][nextIndex]
                heapq.heappush(minHeap, [prevCount, prevTweetId, followeeId, nextIndex - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
