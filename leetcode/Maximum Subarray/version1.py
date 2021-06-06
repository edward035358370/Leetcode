class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def puls(cut,nums):
            if nums == []:
                return []
            elif len(nums) == 1:
                return nums
            a = nums[:cut]
            b = nums[cut:]
            if a == []:
                return [-1000000000,sum(nums[cut:])] + puls(cut-1,nums[:cut]) + puls(1,nums[cut:]) + puls(1,nums[:cut])
            elif b == []:
                return [sum(nums[:cut]),-1000000000000] + puls(cut-1,nums[:cut]) + puls(1,nums[cut:]) + puls(1,nums[:cut])
            return [sum(nums[:cut]),sum(nums[cut:])] + puls(cut-1,nums[:cut]) + puls(1,nums[cut:]) + puls(1,nums[:cut])
        find = []
        if nums == []:
            return 0
        elif len(nums)== 1:
            return nums[0]
        for i in range(len(nums)):
            print(find)
            find += puls(i,nums)
        return max(find)

sol = Solution()
ans = sol.maxSubArray([-2,-1])
print(ans)
