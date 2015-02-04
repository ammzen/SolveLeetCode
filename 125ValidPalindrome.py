# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = self.cleanStr(s)
        if s == '':
            return True
        for x in range(0, len(s)/2 + 1):
            if s[x] != s[-1 - x]:
                return False
        return True

    def cleanStr(self, s):
        cleanstr = ''
        for x in s.upper():
            if x >= 'A' and x <= 'Z' or x >= '0' and x <='9':
                cleanstr += x
        return cleanstr

if __name__ == '__main__':
    s = Solution()
    print s.cleanStr("`l;`` 1o1 ??;l`")
    # print s.isPalindrome('  ')