class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total, count, index = sum(nums), 0, len(nums) - 1
    
        while total % k != 0:
            total -= (nums[index] - 1)
            count += 1
        
        return count
