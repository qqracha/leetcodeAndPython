from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        m = list(s)
        for i in range(len(m)):
            if m[i] == 'I':
                print("find I")
            else:
                print("ne nashli I")

sol = Solution()
print(sol.romanToInt("VIMO"))