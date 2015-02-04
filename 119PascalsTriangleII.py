# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        pascal = []
        row = 0
        while row <= rowIndex:
            if row == 0:
                pascal.append(1)
            else:
                for x in xrange(1, row + 1):
                    if x < row/2.0:
                        pascal[x] = pascal[-x] + pascal[-x-1]
                    elif x == row/2.0:
                        pascal[x] = 2 * pascal[x]
                    else:
                        if x < row:
                            pascal[x] = pascal[row - x]
                        else:
                            pascal.append(pascal[row - x])
            row += 1
        return pascal

if __name__ == '__main__':
    s = Solution()
    print s. getRow(6)       