class Solution(object):
    def removeDuplicates(self, nums):
        temp = []
        index = 0
        while 1 == 1:
            if nums[index] in temp:

                nums.remove(nums[index])

                index -= 1
            else:
                temp.append(nums[index])
            index += 1
            if temp == nums:
                break
        return len(nums),nums

sol = Solution()
ans = sol.removeDuplicates([1,1,1,2,2,23,3,3])
print(ans)