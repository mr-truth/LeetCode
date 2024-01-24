# Given an integer n, return an array ans of length n + 1 such that
# for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        list1 = []

        for i in range(n+1):
            sum_ = bin(i).count("1")
            list1.append(sum_)

        return list1



solution = Solution()
print(solution.countBits(8))