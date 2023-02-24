
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:

    def __init__(self, roman_string: str):
        self.roman_string = roman_string
        self.roman_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XV": 40, "L": 50, "XC": 90, "C": 100,
                           "CD": 400, "D": 500, "CM": 900, "M": 1000}
        self.standart_sum = 0
        self.lst = []

    def roman_to_int(self) -> int:
        for _, __ in enumerate(self.roman_string):
            #
            # Ex:"I"
            #
            if __ == "I" and len(self.roman_string) != (_ + 1):
                if self.roman_string[_ + 1] == "V" or self.roman_string[_ + 1] == "X":
                    pass
                else:
                    self.lst.append(__)
            elif __ == "V" and self.roman_string[_ - 1] == "I" or __ == "X" and self.roman_string[_ - 1] == "I":
                self.lst.append(f"I{__}")
            #
            # Ex:"X"
            #
            elif __ == "X" and len(self.roman_string) != (_ + 1):
                if self.roman_string[_ + 1] == "L" or self.roman_string[_ + 1] == "C":
                    pass
                else:
                    self.lst.append(__)
            elif __ == "L" and self.roman_string[_ - 1] == "X" or __ == "C" and self.roman_string[_ - 1] == "X":
                self.lst.append(f"X{__}")
            #
            # Ex:"C"
            #
            elif __ == "C" and len(self.roman_string) != (_ + 1):
                if self.roman_string[_ + 1] == "D" or self.roman_string[_ + 1] == "M":
                    pass
                else:
                    self.lst.append(__)
            elif __ == "D" and self.roman_string[_ - 1] == "C" or __ == "M" and self.roman_string[_ - 1] == "C":
                self.lst.append(f"C{__}")
            #
            # Fin
            #
            else:
                self.lst.append(__)
        print(self.lst)

    # def roman_to_int(self) -> int:
    #     for _, __ in enumerate(self.roman_string):
    #         #
    #         # Ex:"I"
    #         #
    #         if __ == "I" and len(self.roman_string) != (_ + 1):
    #             if self.roman_string[_ + 1] == "V" or self.roman_string[_ + 1] == "X":
    #                 pass
    #             else:
    #                 self.standart_sum += self.roman_dict[__]
    #         elif self.roman_string[_] == "V" and self.roman_string[_ - 1] == "I" or self.roman_string[_] == "X" and\
    #                 self.roman_string[_ - 1] == "I":
    #             self.standart_sum += (self.roman_dict[__] - self.roman_dict["I"])
    #         #
    #         # Ex:"X"
    #         #
    #         elif __ == "X" and len(self.roman_string) != (_ + 1):
    #             if self.roman_string[_ + 1] == "L" or self.roman_string[_ + 1] == "C":
    #                 pass
    #             else:
    #                 self.standart_sum += self.roman_dict[__]
    #         elif self.roman_string[_] == "L" and self.roman_string[_ - 1] == "X" or self.roman_string[_] == "C" and\
    #                 self.roman_string[_ - 1] == "X":
    #             self.standart_sum += (self.roman_dict[__] - self.roman_dict["X"])
    #         #
    #         # Ex:"C"
    #         #
    #         elif __ == "C" and len(self.roman_string) != (_ + 1):
    #             if self.roman_string[_ + 1] == "D" or self.roman_string[_ + 1] == "M":
    #                 pass
    #             else:
    #                 self.standart_sum += self.roman_dict[__]
    #         elif self.roman_string[_] == "D" and self.roman_string[_ - 1] == "C" or self.roman_string[_] == "M" and\
    #                 self.roman_string[_ - 1] == "C":
    #             self.standart_sum += (self.roman_dict[__] - self.roman_dict["C"])
    #         #
    #         # Fin
    #         #
    #         else:
    #             self.standart_sum += self.roman_dict[__]
    #     print(self.standart_sum)
    #     return self.standart_sum

    def analiz_sum(self):
        for i in self.lst:
            self.standart_sum += self.roman_dict[i]
        print(f"{self.standart_sum}")



sol = Solution("III")
sol.roman_to_int()
sol.analiz_sum()
sol = Solution("LVIII")
sol.roman_to_int()
sol.analiz_sum()
# Output: 58
sol = Solution("MCMXCIV")
sol.roman_to_int()
sol.analiz_sum()
# Output: 1994


sol = Solution("MMMCDXC")
sol.roman_to_int()
sol.analiz_sum()
sol = Solution("MMMMMCDLXIV")
sol.roman_to_int()
sol.analiz_sum()

