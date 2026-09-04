class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org=set(nums)
        x=len(org)
        y=len(nums)
        if x!=y:
            return True
        else:
            return False