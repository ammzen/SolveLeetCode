# Given two sorted integer arrays A and B, merge B into A as one sorted array.

# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i, j, pos = m-1, n-1, m+n
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                pos -= 1
                A[pos] = A[i]
                i -= 1
            else:
                pos -= 1
                A[pos] = B[j]
                j -= 1
        if i < 0:
            A[:pos] = B[:pos]
        return A 

if __name__ == '__main__':
    s = Solution()
    A = []
    m = len(A)
    B = [1]
    n = len(B)
    print s.merge(A,m,B,n)