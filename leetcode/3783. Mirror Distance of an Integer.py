class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse = n - int(str(n)[::-1])
        if reverse < 0:
            return reverse * -1
        else:
            return reverse
