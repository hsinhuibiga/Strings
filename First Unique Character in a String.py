#First Unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - 97] += 1
        for i in xrange(len(s)):
            if letters[ord(s[i]) - 97] == 1:
                return i
        return -1