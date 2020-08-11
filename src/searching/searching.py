# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # print(target, start, end, arr)
    if end >= start:
        mid = (end + start)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, end - 1)
        else:
            return binary_search(arr, target, start + 1, end)
    else:
        return -1




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target, start=0, end=0):
    if (end == 0) and (len(arr) > 0):
        end = len(arr) - 1
    # print(arr, start, end)

    # Your code here

    if end >= start:
        mid = (end + start)//2

        if arr[mid] == target:
            return mid
        # check for ascending or descending
        elif (arr[mid] > target) and (arr[start] < arr[start+1]):
            return agnostic_binary_search(arr, target, start, end - 1)
        elif (arr[mid] < target) and (arr[start] > arr[start+1]):
            return agnostic_binary_search(arr, target, start, end - 1)
        else:
            return agnostic_binary_search(arr, target, start + 1, end)
    else:
        return -1


