class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                total += val_dict[s[i]]
                i += 1
            elif val_dict[s[i]] < val_dict[s[i+1]]:
                total += val_dict[s[i + 1]] - val_dict[s[i]]
                i += 2
            else:
                total += val_dict[s[i]]
                i +=1
        return total


soln = Solution()
ans = soln.romanToInt("MCMXCIV")
print(ans)