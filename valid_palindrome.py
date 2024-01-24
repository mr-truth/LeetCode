# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s:str) -> bool:
        lower_string = s.lower()
        letters = "".join([c for c in lower_string if c.isalnum()])
        if letters == letters[::-1]:
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome("0P"))