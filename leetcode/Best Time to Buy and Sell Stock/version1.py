class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        get = []
        if len(prices) == 2 and prices[1] > prices[0]: return prices[1] -prices[0]
        if len(prices) == 1: return 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] >= 0:
                tempBig = max(prices[i:])

                get.append(tempBig - prices[i-1])
        if get == []: return 0
        return max(get)

sol = Solution()
ans = sol.maxProfit([1,2,3,4,5])
print(ans)