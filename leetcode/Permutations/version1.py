class Solution(object):
    def permute(self, li):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def cut(li,temp,res = []):
            if len(li) == 1:
                res.append(temp + li)

            for i in range(len(li)):
                cut(li[:i]+li[i+1:],temp+[li[i]])
            return res

        return cut(li,[])

li = [1,2,3]
sol = Solution()
ans = sol.permute(li)
print(ans)