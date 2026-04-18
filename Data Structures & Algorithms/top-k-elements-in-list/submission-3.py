class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        # Sort items in 'count' by frequency in descending order
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Add the top k frequent elements to 'ans'
        for i in range(k):
            ans.append(sorted_items[i][0])
        
        return ans


        