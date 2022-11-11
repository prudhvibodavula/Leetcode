def fun1(s):
    l=0
    c=set()
    res=0
    for i in range(len(s)):
        while s[i] in c:
            c.remove(s[i])
            l+=1
        c.add(s[i])
        res=max(res,i-l+1)
    return res
print(fun1("abcabcbb"))
