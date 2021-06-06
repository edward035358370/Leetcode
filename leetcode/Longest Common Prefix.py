class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) > 0 and len(strs)<=200:
            temp = []
            for find in range(1,len(strs[0])+1):
                k = 0
                for finding in range(len(strs)):
                    if strs[0][0:find] == strs[finding][0:find]:
                        print(finding,"==============")
                        print(strs[0][0:find],strs[finding][0:find])
                        k+=1

                if k == len(strs):
                    temp.append(find)
                else:
                    break

            if temp == []:
                return ""
            return strs[0][0:temp[-1]]
        return ""

test = Solution()
solu = test.longestCommonPrefix([])
print(solu)