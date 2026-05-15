class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean = []
        for num in candies:
            if num + extraCandies >= max(candies):
                boolean.append(True)
            else:
                boolean.append(False)

        return boolean
