class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_a =list(str(x))
        list_b = list_a[::-1]
        if list_a == list_b:
            return True
        else:
            return False
        """
        if str(x)[:1] == "-":
            return False
        y = list(str(x))
        z = len(y) // 2
        i = 1
        while i < len(y)-z:
            if y[z - i] == y[z + i]:
                i += 1
            else:
                return False
        return True


        for i in range(len(y)-z):
            i = 1
            if y[z - i] == y[z + i]:
                i += 1
        """





sol = Solution()
print(sol.isPalindrome(303))