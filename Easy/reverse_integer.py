class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(abs(x))
        res = ""
        for i in range(len(x_str)-1, -1, -1):
            res += x_str[i]
        if x < 0:
            int_res = -int(res)
        else:
            int_res = int(res)

        if -2 ** 31 <= int_res <= 2**31-1:
            return int_res
        else:
            return 0

soln = Solution()
ans = soln.reverse(1534236469)
print(ans)