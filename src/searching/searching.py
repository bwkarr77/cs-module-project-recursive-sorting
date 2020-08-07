# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # print(target, start, end, arr)
    # Your code here
    if len(arr) > 0:
        if arr[start] == target:
            return start
        if arr[end] == target:
            return end
        else:
            start += 1
            end -= 1
            return binary_search(arr, target, start, end)
    else:
        return -1



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target, start=0, end=0):
    if start == 0:
        end = len(arr) - 1
    # print(arr, start, end)

    # Your code here
    if (len(arr) > 0) and (start <= end):
        if arr[start] == target:
            # print(start)
            return start
        if arr[end] == target:
            # print(end)
            return end
        else:
            start += 1
            end -= 1
            return agnostic_binary_search(arr, target, start, end)
    else:
        return -1

