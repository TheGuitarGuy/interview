
class Solution:
    def helper(self, i, j):

        if j==0:
            return 0
                
        if j<0 or i<0:
            return 10001
        
        res = min(self.helper(i-1, j), self.helper(i, j-self.coins[i])+1) 
        
        return res

    def coinChange(self, coins: List[int], amount: int) -> int:

        self.coins = coins
        self.amount = amount

        res = self.helper(len(coins)-1, amount)

        if res == 10001:
            return -1
        else:       
            return res
