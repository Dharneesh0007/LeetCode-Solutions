class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        ans = []
        nums1_pt,nums2_pt = 0 ,0

        while nums1_pt < len(nums1) and nums2_pt < len(nums2):
            if nums1[nums1_pt] < nums2[nums2_pt]:
                ans.append(nums1[nums1_pt])
                nums1_pt += 1
            else:
                ans.append(nums2[nums2_pt])
                nums2_pt += 1
        while nums1_pt < len(nums1):
            ans.append(nums1[nums1_pt])     
            nums1_pt += 1
        while nums2_pt < len(nums2):
            ans.append(nums2[nums2_pt])     
            nums2_pt += 1

        if len(ans) %2 != 0:
            return (ans[len(ans)//2])
        return (ans[(len(ans)//2) - 1] + ans[len(ans)//2]) / 2.0  