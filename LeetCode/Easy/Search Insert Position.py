


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target
        for _, __ in enumerate(self.nums):
            if self.target == __:
                print(_)
                return _
            elif self.target < __:
                print(_)
                return _
            elif _ == len(self.nums) - 1:
                print(_ + 1)
                return _ + 1
            elif self.target > __ and _ != len(self.nums) - 1:
                pass

sol = Solution()
sol.searchInsert(nums=[1, 3, 5, 6], target=5)
sol.searchInsert(nums=[1, 3, 5, 6], target=2)
sol.searchInsert(nums=[1, 3, 5, 6], target=7)


