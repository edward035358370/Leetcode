class Solution(object):
    def fib(self, n):
        def puls_list(temp,n):
            if n <= 1:
                return temp[n]
            temp = [temp[1],temp[0] +temp[1]]
            return puls_list(temp,n-1)
        return puls_list([0,1],n)






sol = Solution()
ans = sol.fib()
print(ans)
