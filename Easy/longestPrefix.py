class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = len(min(sorted(strs), key = lambda x: len(x)))
        i = 0
        prefix = ""
        while i < min_length:
            curr_char = strs[0][i]
            should_add = True
            for str in strs:
                if str[i] != curr_char:
                    should_add = False
                    break
            if not should_add:
                break
            else:
                prefix += curr_char
            i += 1
        return prefix


soln = Solution()
ans = soln.longestCommonPrefix(["dog","racecar","car"])
print(ans)

