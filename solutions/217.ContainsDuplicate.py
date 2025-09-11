from typing import Optional, List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        clear = set(nums)
        if len(clear) == len(nums):
            return False
        else:
            return True




sol = Solution()
print(sol.containsDuplicate([1, 2, 3 ,1]))


# big_list = [1,2,3,1]
# big_set = set(big_list)
# def smart():
#     if len(big_set) == len(big_list):
#         return False
#     else:
#         return True

# mem = smart
# print(mem)