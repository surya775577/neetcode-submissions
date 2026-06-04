class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=len(s)
        y=len(t)

        arr=[0]*26

        if x!=y:
            return False

        for i in range(len(s)):
            arr[ord(s[i])-ord('a')]+=1
            arr[ord(t[i])-ord('a')]-=1
        
        for i in arr:
            if i!=0:
                return False
        return True