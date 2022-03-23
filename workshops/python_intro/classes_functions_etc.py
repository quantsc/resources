import heapq

class Asset:
    bids = []
    asks = []
    valueGuesstimate = 0

    def __init__(self):
        heapq.heapify(self.bids)
        heapq.heapify(self.asks)
        return
    
    def newBid(self, price):
        self.updateValueGuess(price)
        heapq.heappush(self.bids, -1*price)

    def updateValueGuess(self, price):
        totalBidsAndAsks = len(self.bids) + len(self.asks)
        self.valueGuesstimate = (self.valueGuesstimate*(totalBidsAndAsks) + price) / (totalBidsAndAsks + 1)

    def newAsk(self, price):
        self.updateValueGuess(price)
        heapq.heappush(self.asks, price)



def main():
    apple = Asset()
    
    apple.newBid(100)
    apple.newAsk(110)
    apple.newBid(105)
    apple.newAsk(115)

    print('apple value guesstimate', apple.valueGuesstimate)
    print('apple asks and bids', apple.asks, apple.bids)
    print()

    cisco = Asset()
    
    cisco.newBid(55)
    cisco.newAsk(52)
    cisco.newBid(57)
    cisco.newAsk(59)

    print('cisco value guesstimate', cisco.valueGuesstimate)
    print('cisco asks and bids', cisco.asks, cisco.bids)

if __name__ == "__main__":
    main()