# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1.
#
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:

        fib_0 = 0
        fib_1 = 1

        if n == 0:
            return fib_0

        if n == 1:
            return fib_1

        for i in range(2, n+1):
            fib_0, fib_1 = fib_1, fib_0 + fib_1

        return fib_1

solution = Solution()
print(solution.fib(50))