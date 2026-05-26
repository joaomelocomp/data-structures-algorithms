class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        x = []
        for num in boxes:
            x.append(int(num))
        
        indexWithOne = []
        for i in range(len(x)):
            if x[i] == 1:
                indexWithOne.append(i)
        
        output = []
        for i in range(len(x)):
            moves = 0
            for j in indexWithOne:
                moves += abs(i - j)
            output.append(moves)
        
        return output #25/05
