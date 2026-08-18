class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=len(s)
        y=len(t)

        if x!=y:
            return False 
        s=''.join(sorted(s,key=str.lower))
        t=''.join(sorted(t,key=str.lower))
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False 
                break 
        return True 
        
