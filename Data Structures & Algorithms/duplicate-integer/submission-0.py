class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        flag=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                flag=0
        if flag:
            return False
        else:
            return True