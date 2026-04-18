class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums =sorted(nums)
        counter = {}
        ans=[]
        for i in nums:
            if i in counter:
                counter[i]+=1
            elif i not in counter:
                counter[i]=1
        # Sort the dictionary items by frequency in descending order
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans