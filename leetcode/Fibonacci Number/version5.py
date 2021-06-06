class Solution(object):
    def fib(self, n):
        def F(n,memo = {}): #because memo is called by reference
            if n <= 1:
                return n
            if n not in memo:
                memo[n] = F(n-1,memo) + F(n-2,memo)
            return memo[n]

        return F(n)


sol = Solution()
ans = sol.fib(10)
print(ans)