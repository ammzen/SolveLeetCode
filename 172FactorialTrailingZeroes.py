# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n < 5:
            return 0
        else:
            return n / 5 + self.trailingZeroes(n / 5)    

if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes(120)
