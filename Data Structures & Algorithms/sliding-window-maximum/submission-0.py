class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        maxlist=[]
        while r<len(nums):
            subarray=nums[l:r+1]
            maxnum = max(subarray)
            maxlist.append(maxnum)
            l+=1
            r+=1
        return maxlist

