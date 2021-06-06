class Solution(object):
    def longestCommonPrefix(self, strs):
        def cut(Str, pos1, pos2, depth, memo={}):

            if (pos1, pos2, Str) in memo:
                if depth == 0:
                    return memo[pos1, pos2, Str]
                else:
                    return []

            if pos1 < 0 or abs(pos1 - pos2) < 1:
                return []

            memo[pos1, pos2, Str] = [Str[pos1:pos2]] + cut(Str, pos1 - 1, pos2, depth + 1, memo) + cut(Str, pos1,
                                                                                                       pos2 - 1,
                                                                                                       depth + 1, memo)

            return memo[pos1, pos2, Str]

        if len(strs) > 0 and len(strs) <= 200:

            temp = []
            for i in range(len(strs)):
                if len(strs[i]) == 1:
                    temp.append([strs[i]])
                else:
                    temp.append([cut(strs[i], len(strs[i]) - 1, len(strs[i]), 0)])

            for finding in range(len(strs)):
                temp[0].append([])
                for find in range(len(temp[0][finding - 1])):
                    if temp[0][finding - 1][find] in temp[finding][0]:
                        temp[0][finding].append(temp[0][finding - 1][find])
            temp_len = []
            all = {}
            for i in temp[0][finding]:
                temp_len.append(len(i))
                all[len(i)] = i
            try:
                return all[max(temp_len)]
            except:
                return ""

        else:
            return ""

test = Solution()
solu = test.longestCommonPrefix(["dog","racecar","car"])
print(solu)