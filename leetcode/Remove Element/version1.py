class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = 0
        key = 0
        i = 0
        length = len(nums)
        tr = True
        while tr == True:
            if nums[i] != val:
                ans += 1
                i += 1
            elif nums[i] == val:
                nums.pop(i)
                key += 1
            if key + i == length:
                print(nums)
                tr = False

        return ans

nums = [0,1,2,2,3,0,4,2]
val = 2
ans =Solution()
print(ans.removeElement(nums,val))