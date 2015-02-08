# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    # @return a boolean
    def isValid(self, s):
        d = {')':'(', ']':'[', '}':'{',}
        stack = []
        for x in s:
            if x=='(' or x=='[' or x=='{':
                stack.append(x)
            else:
                try:
                    if d[x] != stack.pop():
                        return False
                except :
                    return False
        return not stack

if __name__ == '__main__':
    s = Solution()
    print s.isValid('([{}])')