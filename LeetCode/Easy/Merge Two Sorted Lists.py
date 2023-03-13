

import pandas as pd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def merge_two_list(self, list1, list2):
    #     self.list1 = list1
    #     self.list2 = list2
    #     self.lst = []
    #     n, m = len(self.list1), len(self.list2)
    #     i = j = 0
    #
    #     while i < n and j < m:
    #         if self.list1[i] < self.list2[j]:
    #             self.lst.append(self.list1[i])
    #             i += 1
    #         else:
    #             self.lst.append(self.list2[j])
    #             j += 1
    #     while j < m:
    #         self.lst.append(self.list2[j])
    #         j += 1
    #     while i < n:
    #         self.lst.append(self.list1[i])
    #         i += 1
    #     return self.lst
    #
    # def mergeTwoLists(self, lst_add):
    #     if len(lst_add) == 1:
    #         return lst_add
    #     middle = len(lst_add)//2
    #     left = self.mergeTwoLists(lst_add[:middle])
    #     right = self.mergeTwoLists(lst_add[middle:])
    #     return self.merge_two_list(left, right)

    def mergeTwoLists(self, list1, list2):
        lst_upd = []
        if len(list1) == 1 or len(list2) == 1:
            return lst_add
        middle = len(lst_add)//2
        left = self.mergeTwoLists(lst_add[:middle])
        right = self.mergeTwoLists(lst_add[middle:])
        return self.merge_two_list(left, right)


sol = Solution()
# sol.merge_two_list([1, 2, 4], [1, 3, 4])
print(sol.mergeTwoLists(sol.merge_two_list([1, 2, 4], [1, 3, 4])))
# sol.merge_two_list([], [0])

# sol = Solution()
# sol.mergeTwoLists(list2, list2)
