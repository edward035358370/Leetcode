class Solution:
    def combinationSum(self, candidates, target):
        def dfs(target, index):
            if target == 0:
                return [[]]
            elif target < 0:
                return []
            ans = []
            for i in range(index, len(candidates)):
                for nums in dfs(target - candidates[i], i):
                    print(nums)
                    ans.append([candidates[i]] + nums)
            return ans
        return dfs(target, 0)


candidates, target = [2,2,3], 7

sol = Solution()
ans = sol.combinationSum(candidates, target)
print(ans)