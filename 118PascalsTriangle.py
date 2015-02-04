# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        i = 0
        pascal = []
        while i < numRows:
            if i == 0:
                pascal.append([1])
            elif i == 1:
                pascal.append([1, 1])
            else:
                tempstr = []
                tempstr.append(1)
                for x in xrange(1, i):
                    tempstr.append(pascal[i - 1][x - 1] + pascal[i - 1][x])
                tempstr.append(1)
                pascal.append(tempstr)
            i = i + 1
            # print [x for x in pascal].pop()
        return pascal

if __name__ == '__main__':
    s = Solution()
    print s.generate(5)
