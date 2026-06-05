class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map1={}
        n=len(nums)
        for num in nums:
            if num not in map1:
                map1[num]=1
            else:
                map1[num]+=1
            
            if map1[num]>n//2:
                return num 
        
        