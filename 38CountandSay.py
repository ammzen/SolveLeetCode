# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

class Solution:
    # @return a string
    def countAndSay(self, n):
        i, string = 1, '1'
        while i < n:
            prebit, npb, newstr = string[0], 1, ''
            for x in xrange(1, len(string)):
                if string[x] == prebit:
                    npb += 1
                else:
                    newstr += str(npb) + prebit
                    prebit, npb = string[x], 1
            newstr += str(npb) + prebit            
            string = newstr
            i += 1
        return string

if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(7)

