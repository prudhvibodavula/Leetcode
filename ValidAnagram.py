#TC: O(s+t) SC: O(s+t)
def fun1(s,t):
    if len(s)!=len(t):
        return False
    hm1,hm2={},{}
    for i in range(len(s)):
        hm1[s[i]]=1+hm1.get(s[i],0)
        hm2[t[i]] = 1 + hm2.get(t[i], 0)
    return hm1==hm2
print(fun1("rat","car"))

#Also try
#TC : O(nlogn) SC:O(1)
#return sorted(s)==sorted(t)