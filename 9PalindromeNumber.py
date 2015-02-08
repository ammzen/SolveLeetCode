# Determine whether an integer is a palindrome. Do this without extra space.

class Solution:
    # @return a boolean
    def isPalindrome1(self, x):
        if x < 0 or x % 10 == 0 and x:
            return False
        xhalf = 0
        while x > xhalf:
            xhalf = xhalf * 10 + x % 10
            x /= 10
        return (x == xhalf or x == xhalf/10
)
    def isPalindrome(self, x):
        if x < 0:
            return False
        size, xreverse = x, 0
        while size:
            xreverse = xreverse * 10 + size % 10
            size = (size - (size % 10)) / 10 
        return True if xreverse==x else False

if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome1(0)