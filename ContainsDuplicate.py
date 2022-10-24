#Solve using two loops
#TC:O(n^2) SC:O(1)
nums = [1,2,3,1]
#nums = [1,1,1,3,3,4,3,2,4,2]
#nums=[1,2,3,4]
def fun1(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False
print(fun1(nums))

#Solving using sorting TC:O(nlogn) SC:O(1)
def fun2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False
print(fun2(nums))

#Solve using hashmap TC:O(n) SC:O(n)
def fun3(nums):
    hm={}
    for i in nums:
        if i in hm:
            return True
        else:
            hm[i]=1
    return False
print(fun3(nums))

#solve using set TC:O(n) SC:O(n)
def fun4(nums):
    s=set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False
print(fun4(nums))

#also try return len(nums) != len(set(nums))