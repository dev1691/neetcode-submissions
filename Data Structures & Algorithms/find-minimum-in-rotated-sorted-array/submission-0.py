class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        curr_min=float("inf")
        while l<r:
            k=l+(r-l)//2
            curr_min=min(curr_min,nums[k])
            if nums[k]>nums[r]:
                l=k+1
            else:
                r=k-1
        return min(curr_min,nums[l])

