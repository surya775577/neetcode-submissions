class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1={}

        for num in nums:
            if num not in map1:
                map1[num]=1
            else:
                map1[num]+=1
        
        for i,j in map1.items():
            if j>1:
                return True 
                break
        return False