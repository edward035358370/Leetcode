class Solution(object):
    def fib(self, n):
        def pulse(a,b,n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            elif n == 2:
                return a+b
            return pulse(b,a+b,n-1)
        return pulse(0,1,n)

sol = Solution()
ans = sol.fib()
print(ans)