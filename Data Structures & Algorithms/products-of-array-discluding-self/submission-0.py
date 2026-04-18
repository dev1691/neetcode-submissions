from functools import reduce
from operator import mul
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[reduce(mul, [x for j, x in enumerate(nums) if j != i], 1) for i in range(len(nums))]
        return output