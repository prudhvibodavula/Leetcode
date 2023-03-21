class Solution:
    def rob(self, nums: List[int]) -> int:
        val1,val2=0,0
        for i in nums:
            tmp=max(i+val1,val2)
            val1=val2
            val2=tmp
        return val2
