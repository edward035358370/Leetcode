# Definition for singly-linked list.
#class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        compare = len(l1) - len(l2)
        if compare >= 0:
            for key in range(len(l2)):
               res.append(l1[key] + l2[key])
            for key in range(len(l2),len(l1)):
                res.append(l1[key])
        else:
            for key in range(len(l1)):
               res.append(l1[key] + l2[key])
            for key in range(len(l1),len(l2)):
                res.append(l2[key])
        for index in range(len(res)):

            if res[index] >= 10:
                res[index] -= 10
                try:
                    res[index + 1] += 1
                except:
                    res.append(1)
        return res
sol = Solution()
ans = sol.addTwoNumbers([0],[0])
print(ans)
'''