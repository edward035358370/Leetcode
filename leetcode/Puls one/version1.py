class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        def puls(digits, pos):
            digits[pos] += 1
            if digits[pos] == 10:
                digits[pos] = 0
                if pos == 0:
                    digits.insert(0, 1)
                    return digits
                return puls(digits,pos-1)

            return digits

        return puls(digits, len(digits) - 1)

sol = Solution()
ans = sol.plusOne([8,7,4,5,2,6,9,9])
print(ans)