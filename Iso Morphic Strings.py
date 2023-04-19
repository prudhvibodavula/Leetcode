class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm1 = {}
        for i in range(len(s)):
            if s[i] in hm1:
                hm1[s[i]].append(i)
            else:
                hm1[s[i]] = [i]

        hm2 = {}
        for i in range(len(t)):
            if t[i] in hm2:
                hm2[t[i]].append(i)
            else:
                hm2[t[i]] = [i]

        print(hm1)
        print(hm2)
        return list(hm1.values()) == list(hm2.values())

s="name"
print(s.zfill(6))