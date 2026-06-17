class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        cur_s=1
        lon_s=1

        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                cur_s+=1
            else:
                lon_s=max(lon_s,cur_s)
                cur_s=1
        return max(lon_s,cur_s)