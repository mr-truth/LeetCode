# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        s_freq = {}
        t_freq = {}

        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        return s_freq == t_freq

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))