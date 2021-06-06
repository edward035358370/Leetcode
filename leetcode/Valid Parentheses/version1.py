class Solution(object):
    def isValid(self, s):
        def twin(mark):
            if mark == "]":
                return "["
            elif mark == "}":
                return "{"
            elif mark == ")":
                return "("
            else:
                return "False"
        if len(s) <= 10 ** 4 and len(s) >= 1:
            if len(s) % 2 == 1:
                return False
            else:
                memory = []
                for i in range(len(s)):
                    if s[i] == "[" or s[i] == "{" or s[i] == "(":
                        memory.append(s[i])
                    elif s[i] == "]" or s[i] == "}" or s[i] == ")":
                        try:
                            if memory[-1] == twin(s[i]):
                                memory.pop(-1)
                            else:
                                return False
                        except:
                            return False
                if memory == []:
                    return True
                return False
        else:
            return False

sol = Solution()
ans = sol.isValid("([}}])")
print(ans)