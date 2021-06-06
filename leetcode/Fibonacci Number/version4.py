class Solution(object):
    def fib(self, n):
        def F(n):
            if n <= 1:
                return n
            else:
                return F(n-1) + F(n-2)
        return F(n)


sol = Solution()
ans = sol.fib(10)
print(ans)
