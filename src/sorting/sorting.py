# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # print('merge: ', arrA, arrB)
    merged_arr = []
    a_ind = b_ind = 0
    while a_ind < len(arrA) or b_ind < len(arrB):
        if a_ind >= len(arrA):
            merged_arr.append(arrB[b_ind])
            b_ind += 1
        elif b_ind >= len(arrB):
            merged_arr.append(arrA[a_ind])
            a_ind += 1
        elif arrA[a_ind] <= arrB[b_ind]:
            merged_arr.append(arrA[a_ind])
            a_ind += 1
        elif arrA[a_ind] > arrB[b_ind]:
            merged_arr.append(arrB[b_ind])
            b_ind += 1
    return merged_arr


    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) <= 1:
        return arr
    # recursive case
    else:
        mid = len(arr)//2
        # print('merge sort: ', arr, '=> mid: ', mid)
        # recursive loop: reduces "left side" of array until it is only 2 elements
        lh = merge_sort(arr[:mid])
            # recursion: above code repeats until the 'return' line is met
            # then it "pops off" the stack, and continues to the next code
        rh = merge_sort(arr[mid:])
        return merge(lh, rh)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

