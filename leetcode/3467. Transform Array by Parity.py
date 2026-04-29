class Solution:
    def transformArray(self, nums: List[int]) -> List[int]: # type: ignore
        ind = 0
        for number in nums:
            if number % 2 == 0:
                nums[ind] = 0
                ind += 1

        for i in range(ind, len(nums)):
            nums[i] = 1
    
        return nums