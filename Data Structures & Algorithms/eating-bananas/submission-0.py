class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(piles, k, h):
            """
            Helper function to check if all piles can be eaten with speed `k` within `h` hours.
            """
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            return total_hours <= h

        # Initialize binary search bounds
        left, right = 1, max(piles)
        minspeed = right  # Initialize with the maximum possible speed

        while left <= right:
            mid = (left + right) // 2  # Try the middle speed
            if canEatAll(piles, mid, h):
                minspeed = mid  # If can eat all, try slower speed
                right = mid - 1
            else:
                left = mid + 1  # If cannot eat all, try faster speed

        return minspeed
