# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Input: [9,8,7,6,5,4,3,2,1,0] Expected: [9,8,7,6,5,4,3,2,1,1]

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne1(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]
        
    def plusOne(self, digits):
        return self.split(self.assemble(digits) + 1)

    def split(self, integer):
        alist, bits, tmp = [], 1, integer
        while tmp/10:
            bits += 1
            tmp /= 10
        while bits:
            tmp = integer / 10**(bits-1)
            integer -= tmp * 10**(bits-1)
            alist.append(tmp)
            bits -= 1
        return alist

    def assemble(self, alist):
        integer = 0
        for x in alist:
            integer += x * 10**(len(alist)-1)
            alist = alist[1:]
        return  integer

if __name__ == '__main__':
    s = Solution()
    print s.plusOne1([100])