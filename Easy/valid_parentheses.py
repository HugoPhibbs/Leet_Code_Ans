class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        inverse = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        openers = ["(", "[", "{"]
        for i in range(len(s)):
            curr_char = s[i]
            if curr_char in openers:
                stack.append(curr_char)
            elif len(stack) == 0:
                return False
            elif stack[-1] == inverse[curr_char]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

soln = Solution()
ans = soln.isValid("]")
print(ans)



