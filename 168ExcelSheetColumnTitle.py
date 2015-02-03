# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 

class Solution:
    # @return a string
    def convertToTitle(self, num):
        d = {1 :'A', 2 :'B', 3 :'C', 4 :'D', 5 :'E', 6 :'F', 7 :'G', 8 :'H', 9:'I',
             10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q',
             18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
        string = ''
        bitnum = num
        while bitnum > 26:
            i = 0
            num = bitnum
            while bitnum > 26:
                if bitnum % 26 == 0:
                    bitnum = bitnum - 1
                bitnum /= 26
                i = i + 1
            string += d[bitnum]
            bitnum = num - 26 ** i * bitnum
        string += d[bitnum]
        return string

if __name__ == '__main__':
    s = Solution()
    print s.convertToTitle(52)