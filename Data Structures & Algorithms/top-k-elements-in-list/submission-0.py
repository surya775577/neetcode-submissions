class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1={}
        for num in nums:
            if num not in map1:
                map1[num]=1
            else:
                map1[num]+=1
        items=list(map1.items())

        items.sort(key=lambda x:x[1],reverse=True)

        ans=[]

        for i in range(k):
            ans.append(items[i][0])
        
        return ans 
