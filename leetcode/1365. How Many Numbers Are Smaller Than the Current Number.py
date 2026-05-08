class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        for number in nums:
            count_number = 0
            for j in range(len(nums)):
                if number > nums[j]:
                    count_number += 1
            count.append(count_number)

        return count
