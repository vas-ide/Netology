
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:

    def __init__(self, roman_string: str):
        self.roman_string = roman_string
        self.roman_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100,
                           "CD": 400, "D": 500, "CM": 900, "M": 1000}
        self.standart_sum = 0
        self.lst_inf = []

    def analiz(self):
        for _, __ in enumerate(self.roman_string):
            if __ == "I":
                if len(self.roman_string) != _ + 1:
                    if self.roman_string[_ + 1] == "V" \
                            or self.roman_string[_ + 1] == "X":
                        pass
                    else:
                        self.lst_inf.append(__)
                else:
                    self.lst_inf.append(__)
            elif __ == "V" and self.roman_string[_ - 1] == "I" and _ != 0\
                    or __ == "X" and self.roman_string[_ - 1] == "I" and _ != 0:
                self.lst_inf.append(f"{self.roman_string[_ - 1]}{__}")
            elif __ == "X":
                if len(self.roman_string) != _ + 1:
                    if self.roman_string[_ + 1] == "L" or self.roman_string[_ + 1] == "C":
                        pass
                    else:
                        self.lst_inf.append(__)
                else:
                    self.lst_inf.append(__)
            elif __ == "L" and self.roman_string[_ - 1] == "X" and _ != 0\
                    or __ == "C" and self.roman_string[_ - 1] == "X" and _ != 0:
                self.lst_inf.append(f"{self.roman_string[_ - 1]}{__}")
            elif __ == "C":
                if len(self.roman_string) != _ + 1:
                    if self.roman_string[_ + 1] == "D" or self.roman_string[_ + 1] == "M":
                        pass
                    else:
                        self.lst_inf.append(__)
                else:
                    self.lst_inf.append(__)
            elif __ == "D" and self.roman_string[_ - 1] == "C" and _ != 0\
                    or __ == "M" and self.roman_string[_ - 1] == "C" and _ != 0:
                self.lst_inf.append(f"{self.roman_string[_ - 1]}{__}")
            else:
                self.lst_inf.append(__)





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
        print(self.lst_inf)
        for i in self.lst_inf:
            self.standart_sum += self.roman_dict[i]
        print(f"{self.standart_sum}")

sol = Solution("MCIV")
sol.analiz()
sol.analiz_sum()
sol = Solution("III")
sol.analiz()
sol.analiz_sum()
sol = Solution("LVIII")
sol.analiz()
sol.analiz_sum()
sol = Solution("MCMXCIV")
sol.analiz()
sol.analiz_sum()
sol = Solution("MMMCDXC")
sol.analiz()
sol.analiz_sum()
sol = Solution("CDLXIX")
sol.analiz()
sol.analiz_sum()
sol = Solution("XCII")
sol.analiz()
sol.analiz_sum()
