# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution():
    def removeElement(self, A, elem):
        i, j, count = 0, len(A)-1, 0
        while i < j:
            if A[i] != elem and A[j] != elem:
                i, j = i + 1, j
            elif A[i] != elem and A[j] == elem:
                i, j, count = i + 1, j - 1, count + 1                
            elif A[i] == elem and A[j] != elem:
                A[i], A[j] = A[j], A[i]
                i, j, count = i + 1, j - 1, count + 1
            else:
                i, j, count = i, j - 1, count + 1
            print A
        if i == j and A[i] == elem:
            count += 1
        return len(A) - count

if __name__ == '__main__':
    s = Solution()
    A = [1,1,3]
    elem = 1
    print s.removeElement(A, elem)