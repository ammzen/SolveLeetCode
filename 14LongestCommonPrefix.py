# Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not len(strs):
            return ''
        for x in strs:
            if not len(x):
                return ''
        mini = len(strs[0])
        prefix = ''
        for x in xrange(1, len(strs)):
            if len(strs[x]) < mini:
                mini = len(strs[x])
        for i in xrange(mini):
            prefix += strs[0][i] 
            for x in xrange(1, len(strs)):
                if strs[x][i] != strs[0][i]:
                    return prefix[:-1]
        return prefix

if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(['abc', 'abcde', 'abcfil', 'abc'])