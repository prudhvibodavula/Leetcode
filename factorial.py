# using recursion

def fact(n):
    #Base case
    if n<=1:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))