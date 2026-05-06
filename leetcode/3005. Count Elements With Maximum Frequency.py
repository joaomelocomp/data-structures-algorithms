##You are given an array nums consisting of positive integers.
##Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
##The frequency of an element is the number of occurrences of that element in the array.

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        appears = {}

        for num in nums:
            if num in appears:
                appears[num] += 1
            else:
                appears[num] = 1
        
        max_aps = 0    
        aps = list(appears.values())
        max_aps = max(aps)

        #biggest value in the dict
        overall = []
        for num in appears.values():
            if num == max_aps:
                overall.append(num)
        
        return sum(overall)
