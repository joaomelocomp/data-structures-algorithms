class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        all = []
        for num in nums:
            all.append(num)
        for num in (reversed(nums)):
            all.append(num)
        return all
