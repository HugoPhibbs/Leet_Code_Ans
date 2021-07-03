class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        res = ""
        for i in range(len(x_str)-1, -1, -1):
            res += x_str[i]
        return res == x_str

soln = Solution()
ans = soln.isPalindrome(-121)
print(ans)
