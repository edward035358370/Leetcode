class Solution:
    def combinationSum(self, candidates,target):
        ans = []
        def dfs(target, _list):
            print(_list)
            if(target == 0):
                ans.append(_list)
            elif(target < 0):
                return None
            for n in candidates:
                if((len(_list) >= 1 and _list[-1] <= n) or len(_list) == 0):
                    dfs(target - n, _list + [n])
        dfs(target, [])
        return ans


candidates, target = [2,3], 7

sol = Solution()
ans = sol.combinationSum(candidates, target)
print(ans)