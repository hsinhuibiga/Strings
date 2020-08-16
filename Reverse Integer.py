#Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        r = int(str(x)[::-1])
        if flag == 1 and r <= 2147483647:
            return r
        elif flag == -1 and -r >= -2147483648:
            return -r
        return 0