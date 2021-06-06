class Solution:
    def maxProfit(self, prices):
        min_ = float("inf")
        ans = 0
        for i in range(len(prices)):
            if prices[i] <= min_:
                min_ = prices[i]
            elif prices[i] - min_ >= ans:
                ans = prices[i] - min_
        return ans

sol = Solution()
ans = sol.maxProfit([7,1,5,3,6,4])
print(ans)