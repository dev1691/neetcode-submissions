class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            if len(stones)==0:
                return 0
            if len(stones)==1:
                return stones[0]
            x=stones.pop()
            y=stones.pop()
            if x==y:
                continue
            if x>y:
                x=x-y
                stones.append(x)
                stones.sort()
        if len(stones)==0:
                return 0
        if len(stones)==1:
            return stones[0]
        