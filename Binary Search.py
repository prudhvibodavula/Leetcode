# Recursive Approach
def BinarySearch_Recursive(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return BinarySearch_Recursive(arr, low, mid - 1, target)
        else:
            return BinarySearch_Recursive(arr, mid + 1, high, target)
    else:
        return -1


arr = [1, 2, 3, 4, 5]
x = 5
print(BinarySearch_Recursive(arr, 0, len(arr) - 1, x))


# Iterative Approach

def BinarySearch_Iterative(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1


print(BinarySearch_Iterative(arr, x))
