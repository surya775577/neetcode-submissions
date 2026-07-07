class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x=len(nums)
        flag=0
        res=0
        for i in range(x):
            if nums[i]==target:
                flag=1 
                res=i
                break
            else:
                flag=0
        if flag==1:
            return res
        else: 
            return -1
