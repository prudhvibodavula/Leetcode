arr=[2,3,-2,4]
res=1
m=1000000
for i in range(len(arr)):
    for j in range(i,len(arr)):
        res *=arr[i]*arr[j]
        if m<res:
            res=m
        res=1
print(res)