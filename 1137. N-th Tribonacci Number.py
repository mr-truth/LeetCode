# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.


class Solution:
    def tribonacci(self, n: int) -> int:
        trib_lst = [0] * (n+1)

        if n == 0 or n == 1:
            return n

        if n == 2:
            return 1

        trib_lst[0] = 0
        trib_lst[1] = 1
        trib_lst[2] = 1

        for i in range(0, n-2):
            trib_lst[i+3] = trib_lst[i] + trib_lst[i+1] + trib_lst[i+2]

        return trib_lst[n]

solution = Solution()
print(solution.tribonacci(4))