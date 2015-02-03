# PROBLEM DESCRIPTION
# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

# Here is an example of version numbers ordering:

# 0.1 < 1.1 < 1.2 < 13.3.7

import string
import time
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        if version1 == version2:
            return 0
        f11 = splitByFlag(version1)[1]
        f12 = splitByFlag(version1)[2]
        f21 = splitByFlag(version2)[1]
        f22 = splitByFlag(version2)[2]
        while f12 != '0' or f22 != '0' :
            # print '%s %s , %s %s' %(f11,f12, f21,f22)
            if string.atoi(f11) > string.atoi(f21):
                return 1
            elif string.atoi(f11) < string.atoi(f21):
                return -1
            else:
                return self.compareVersion(f12, f22)
        return cmp(string.atoi(f11), string.atoi(f21))

def splitByFlag(str1, flag='.'):
    for x in range(0, len(str1)):
        if str1[x] == flag:
            return [x, str1[0:x], str1[x+1:]]
    return [len(str1) + 1, str1, '0']

if __name__ == '__main__':
    start = time.time()
    for x in range(1000):
        s = Solution()
        s.compareVersion('1.0.1.00', '1')
    print (time.time() - start)/1000
