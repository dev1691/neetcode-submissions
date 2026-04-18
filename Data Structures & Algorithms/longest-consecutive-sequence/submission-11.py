class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        # nums=list(set(nums))
        print(nums)
        longest_seq=set()
        longest_seq.add(nums[0])
        curr_seq=set()
        curr_seq.add(nums[0])
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                curr_seq.add(nums[i])                
            if len(longest_seq)<len(curr_seq):
                longest_seq=curr_seq
            if nums[i]-nums[i-1]>1:
                curr_seq=set()
                curr_seq.add(nums[i])
        return len(longest_seq)

                
        