class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recc_search(nums, target, index):
            if not nums:  # base case: if nums is empty
                return -1
            if len(nums) == 1:
                return index if nums[0] == target else -1
            
            # Find the midpoint to split the list
            hlf_pt = len(nums) // 2
            nums1 = nums[:hlf_pt]
            nums2 = nums[hlf_pt:]

            # Recursively search in the first half
            result1 = recc_search(nums1, target, index)
            if result1 != -1:  # if found in the first half, return the index
                return result1
            
            # Recursively search in the second half
            result2 = recc_search(nums2, target, index + hlf_pt)
            return result2  # return the result from the second half (could be -1 if not found)

        # Start the recursive search from index 0
        return recc_search(nums, target, 0)