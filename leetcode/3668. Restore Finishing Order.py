class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        out = []
        for number in order:
            if number in friends:
                out.append(number)
    
        return out
