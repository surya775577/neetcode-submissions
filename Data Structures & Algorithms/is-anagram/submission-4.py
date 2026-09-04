class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1_l=len(s)
        str2_l=len(t)

        if str1_l!=str2_l:
            return False 

        str1=sorted(s)
        str2=sorted(t)

        for i in range(str1_l):
            if str1[i]!=str2[i]:
                return False 
                break 
        return True
