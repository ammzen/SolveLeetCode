# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        n1, n2 = 1, 2
        for x in xrange(n, 2, -1):
            sum = n1 + n2
            n1 = n2
            n2 = sum
        return sum
    
if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(35)#14930352