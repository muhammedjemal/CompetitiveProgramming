class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        my_coins = 0
        piles.sort()
        for i in range(len(piles)//3):
            my_coins += piles[-2 - 2*i]
        
        return my_coins
