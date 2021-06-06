class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        route = []
        def goto(candidates,target,route,res = []):
            if target == 0:
                res.append(route)
            print(target, route)
            for i in range(len(candidates)):
                temp = candidates[i]
                if target - temp >= 0:
                    goto(candidates,target-temp,route + [temp])


            return res

        res = goto(candidates, target, route)
        for sorting in range(len(res)):
            res[sorting].sort()

        if len(res) > 0:
            real_res = [res[0]]
            for remove in range(1, len(res)):
                if res[remove] not in real_res:
                    real_res.append(res[remove])
            if [] in real_res:
                real_res.remove([])

            return real_res
        else:
            if [] in res:
                res.remove([])
            return res


candidates, target = [2,2,3,7], 7

sol = Solution()
ans = sol.combinationSum(candidates, target)
print(ans)