class Solution:
    def scoreOfString(self, s: str) -> int:
        x = list(map(ord, s))
        totalSum = sum(abs(x[i]-x[i+1]) for i in range(len(x)-1))
        return totalSum

sol = Solution()
print(sol.scoreOfString("hello"))