class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2 
        nums.sort()
        res=0

        x=len(nums)

        if x%2==0:
            dem1=(x//2)-1
            res=(nums[dem1]+nums[dem1+1])/2
        else:
            middle=x//2
            res=float(nums[middle])
        return res