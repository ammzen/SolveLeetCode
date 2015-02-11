# -*- coding: utf-8 -*- 
# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        hlen, nlen = len(haystack), len(needle)
        i, rightshift, strfeature = 0, nlen, self.strFeature(needle)
        while i <= hlen - nlen:
            j = nlen - 1
            while j >= 0:
                if needle[j] == haystack[i + j]:
                    j -= 1
                else:
                    if i + nlen > hlen - 1:
                        return -1
                    rightshift = nlen - strfeature[ord(haystack[i + nlen])]
                    # rightshift = nlen - search(needle, haystack[i + nlen])
                    break
            if j < 0:
                return i
            i += rightshift
        return -1

    def strFeature(self, string):
        if string == '':
            return []
        feature = [-1 for i in xrange(0,256)]
        for i,x in enumerate(string):
            feature[ord(x)] = i
        return feature

def search(string, s):
    i = len(string)
    for x in xrange(i-1, -1, -1):
        if string[x] == s:
            return x
    return -1


if __name__ == '__main__':
    s = Solution()
    print s.strStr('aa', 'aaa')
    print s.strStr("mississippi", "a")
    print s.strStr("mississippi", '')
    print s.strStr("mississippi", "issipi")
    print s.strStr("mississippi", "issip")
    print s.strStr("mississippi", "a")
    print s.strStr("hellphelloaaa", "hello")
    print s.strStr("babaabcbbabb", "bbab")