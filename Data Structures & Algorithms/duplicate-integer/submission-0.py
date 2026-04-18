class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return False
        numset=set()
        for n in nums:
            if n not in numset:
                numset.add(n)
            else:
                return True
        return False

        
         