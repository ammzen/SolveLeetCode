# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution:
    # @return an integer
    def reverse1(self, x):
        ret, i, s = 0, abs(x), -1 if x < 0 else 1
        while i:
            i, ret = i//10, ret * 10+ i%10
        return 0 if ret > pow(2, 31) else ret * s

    def reverse(self, x):
        abx = abs(x)
        absx = abx
        s = 0
        i = 0
        while abx/10:
            i += 1
            abx /= 10
        while absx:
            ln = absx % 10
            absx = (absx - ln) / 10
            s += ln * 10**i
            i -= 1
        if s > 2**31 - 1 or s < -2**31:
            return 0
        if x >= 0:
            return s
        else:
            return -s

if __name__ == '__main__':
    s = Solution()
    print s.reverse1(6271)