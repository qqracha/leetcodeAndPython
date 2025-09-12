# from typing import Optional, List

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()

#         for i, v in enumerate(nums):

#             if (i != v):
#                 return v - 1
            
#             if v == len(nums) - 1:
#                 return v + 1


# sol = Solution()
# nums = [0,3,2]
# print(sol.missingNumber(nums))

nums = [0,1,2,3]

print(sum(range(len(nums)+1)))