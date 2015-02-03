# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        if len(num) == 1:
            return num[0]
        me = num[0]
        count = 1
        for x in range(1, len(num)):
            if num[x] != me:
                count = count - 1
                if count == 0:
                    me = num[x]
                    count = 1
            else:
                count = count + 1
        return me

if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([6, 6, 7, 7, 7])
