class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol=[]
        
        for i in range(len(nums)):
            ans=1
            for j in range(len(nums)):
                if i!=j:
                    ans*=nums[j]
            sol.append(ans)
        return sol