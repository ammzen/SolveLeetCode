# Implement atoi to convert a string to an integer.

# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.lstrip()
        if str == '' or not str[0].isdigit() and str[0] != '-' and str[0] != '+':
            return 0
        elif str[0] == '-':
            return -self.calStrFromN(str, 1) if -self.calStrFromN(str, 1)>=(-2**31) else -2147483648
        elif str[0] == '+':
            return self.calStrFromN(str, 1) if self.calStrFromN(str, 1)<=(2**31-1) else 2147483647
        else:
            return self.calStrFromN(str, 0) if self.calStrFromN(str, 0)<=(2**31-1) else 2147483647

    def calStrFromN(self, str, i):
        integer = 0
        for x in xrange(i, len(str)):
            if str[x].isdigit():
                integer += (ord(str[x])-ord('0')) * 10**(len(str)-1-x)
            else:
                return integer/10**(len(str)-x)
        return integer


if __name__ == '__main__':
    s = Solution()
    print s.atoi("2147483649")