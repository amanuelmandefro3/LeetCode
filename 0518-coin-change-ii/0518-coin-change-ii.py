class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(1,amount+1):   
                if i-coin >= 0:
                    dp[i] += dp[i-coin]

        return dp[-1]           

        # memo = {}
        # def dp(i,amount):
        #     if amount == 0:
        #         return 1
        #     if amount < 0 or i == len(coins):
        #         return 0 
        #     if (i,amount) not in memo:
        #         memo[(i,amount)] = dp(i, amount-coins[i]) + dp(i+1, amount)      

        #     return memo[(i,amount)]  

        # return dp(0,amount)          

        