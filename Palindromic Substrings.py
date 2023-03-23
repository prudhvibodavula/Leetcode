class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            c+=self.fun(s,i,i)
            c+=self.fun(s,i,i+1)     
        return c

    def fun(self,s,l,r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        return res
