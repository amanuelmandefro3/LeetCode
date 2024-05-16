class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        for i in range(2, n+1):
            first, second = second, first+second
        return second    
        