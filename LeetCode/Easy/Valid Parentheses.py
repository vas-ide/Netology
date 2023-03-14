




class Solution:
    # def isValid(self, s: str) -> bool:
    #     for _, __ in enumerate(s):
    #         if __ == ")" and s[_ - 1] != "(":
    #             print(False)
    #             return False
    #         elif __ == "]" and s[_ - 1] != "[":
    #             print(False)
    #             return False
    #         elif __ == "}" and s[_ - 1] != "{":
    #             print(False)
    #             return False
    #         else:
    #             pass
    #     print(True)
    #     return True

    # def isValid(self, s: str) -> bool:
    #     counter_1 = 0
    #     counter_2 = 0
    #     counter_3 = 0
    #     for _ in s:
    #         if counter_1 > 1 or counter_2 > 1 or counter_3 > 1:
    #             print(False)
    #             return False
    #         elif _ == "(":
    #             if counter_1 == 0 and counter_2 == 0 and counter_3 == 0:
    #                 counter_1 += 1
    #             else:
    #                 print(False)
    #                 return False
    #         elif _ == "[":
    #             if counter_1 == 0 and counter_2 == 0 and counter_3 == 0:
    #                 counter_2 += 1
    #             else:
    #                 print(False)
    #                 return False
    #         elif _ == "{":
    #             if counter_1 == 0 and counter_2 == 0 and counter_3 == 0:
    #                 counter_3 += 1
    #             else:
    #                 print(False)
    #                 return False
    #         elif _ == ")":
    #             if counter_1 == 1 and counter_2 == 0 and counter_3 == 0:
    #                 counter_1 -= 1
    #             else:
    #                 print(False)
    #                 return False
    #         elif _ == "]":
    #             if counter_1 == 0 and counter_2 == 1 and counter_3 == 0:
    #                 counter_2 -= 1
    #             else:
    #                 print(False)
    #                 return False
    #         elif _ == "}":
    #             if counter_1 == 0 and counter_2 == 0 and counter_3 == 1:
    #                 counter_1 -= 1
    #             else:
    #                 print(False)
    #                 return False
    #     print(True)
    #     return True

    def isValid(self, s: str) -> bool:
        for _, __ in enumerate(s):
            lst_open = ["(", "[", "{"]
            lst_closed = [")", "]", "}"]
            mark_1 = 0
            mark_2 = 0
            mark_3 = 0
            if mark_1 == 0:
                if __ == "(":
                    mark_1 += 1
                elif __ == "[":
                    mark_1 += 1
                elif __ == "{":
                    mark_1 += 1
            elif mark_1 == 1 and mark_2 == 0:
                if __ == "(":
                    mark_2 += 1
                elif __ == "[":
                    mark_2 += 1
                elif __ == "{":
                    mark_2 += 1
                elif __ == ")":
                    mark_1 -= 1
                elif __ == "]":
                    mark_1 -= 1
                elif __ == "}":
                    mark_1 -= 1
            elif mark_1 == 1 and mark_2 == :
                if __ == "(":
                    mark_2 += 1
                elif __ == "[":
                    mark_2 += 1
                elif __ == "{":
                    mark_2 += 1
                elif __ == ")":
                    mark_1 -= 1
                elif __ == "]":
                    mark_1 -= 1
                elif __ == "}":
                    mark_1 -= 1





sol = Solution()
sol.isValid("([)]")
sol.isValid('()')
sol.isValid("()[]{}")
sol.isValid("(]")