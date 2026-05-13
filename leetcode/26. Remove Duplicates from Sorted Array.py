class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        no_duplicates = list(sorted(set(nums)))
        for i in range(len(no_duplicates)):
            nums[i] = no_duplicates[i]

        return len(no_duplicates)
