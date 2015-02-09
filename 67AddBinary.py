# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution():
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        digit, string = 0, ''
        if len(a) > len(b):
            b = '0' * (len(a)-len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b)-len(a)) + a
        for x in xrange(len(max(a, b))):
            digit = digit * 2 + (int(a[x]) + int(b[x]))
        if not digit:
            string = '0' 
        while digit:
            string = str(digit%2) + string
            digit /= 2
        return string


if __name__ == '__main__':
    s = Solution()
    print s.addBinary('0', '0')