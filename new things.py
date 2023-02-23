arr=[[3,4],[1,7],[5,6]]
for i,j in arr:
    print(i,j)
arr.sort()
print(arr)
arr.sort(key=lambda k:k[1])
print(arr)