class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        completed = time//(n-1)
        remaining = time % (n-1)
        if(completed % 2):
            return n-remaining
        return remaining + 1    
        