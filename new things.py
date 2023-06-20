a=[1,2]
import copy
b=a
c=copy.deepcopy(b)
a[0]=2
print(a,b,c)

print((1,2)==(2,1))