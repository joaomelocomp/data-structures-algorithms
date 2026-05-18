class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(abs(nums[i]))
            else:
                odd.append(nums[i] * -1)
        
        result = sum(even) + sum(odd)
        return result
