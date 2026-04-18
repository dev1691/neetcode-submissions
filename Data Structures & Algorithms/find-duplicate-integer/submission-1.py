class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        domain=list(range(len(nums)))
        n=len(nums)
        nums.sort()
        visited=set()
        l=0
        r=n-1
        while l<=r:
            if nums[l]==nums[r]:
                return nums[r]
            if nums[l] in visited:
                return nums[l]
            if nums[r] in visited:
                return nums[r]
            visited.add(nums[l])
            visited.add(nums[r])
            l+=1
            r-=1
            
        