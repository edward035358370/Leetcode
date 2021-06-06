class Solution:
    def maxSubArray(self, nums):
        l = len(nums)
        if l == 0: return 0
        res = now = nums[0]
        for i in range(1, l):
            print("res",res,"now",now)
            if now >0:
                now += nums[i]
            else:
                now = nums[i]
            #if now is bigger than res, just puls it.
            #if it is not bigger than res, then don't change.
            #this can make the now keep pulsed but mantain the biggest result.
            if now > res:
                res = now
        return res
sol = Solution()
ans = sol.maxSubArray([-7,1,5,-11,6,4])
print(ans)












