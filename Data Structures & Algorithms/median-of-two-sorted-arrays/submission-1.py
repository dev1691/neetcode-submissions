class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = 0
        l2 = 0
        k = (len(nums1) + len(nums2)) // 2
        new_arr = []
        
        while l1 < len(nums1) and l2 < len(nums2) and len(new_arr) <= k:
            if nums1[l1] < nums2[l2]:
                new_arr.append(nums1[l1])
                l1 += 1
            else:
                new_arr.append(nums2[l2])
                l2 += 1
        
        # If one of the arrays is exhausted
        while l1 < len(nums1) and len(new_arr) <= k:
            new_arr.append(nums1[l1])
            l1 += 1
        
        while l2 < len(nums2) and len(new_arr) <= k:
            new_arr.append(nums2[l2])
            l2 += 1
        
        # Calculate the median
        if (len(nums1) + len(nums2)) % 2 != 0:
            return float(new_arr[k])
        else:
            return float((new_arr[k] + new_arr[k - 1]) / 2)
