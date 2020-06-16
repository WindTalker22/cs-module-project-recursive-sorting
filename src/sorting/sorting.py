# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(Left, Right):
    # elements = len(Left) + len(Right)
    # Left index, and right index
    left_ind = 0
    right_ind = 0
    combined = []

    while left_ind < len(Left) and right_ind < len(Right):
        if Left[left_ind] < Right[right_ind]:
            combined.append(Left[left_ind])
            left_ind += 1
        else:
            combined.append(Right[right_ind])
            right_ind += 1

    while left_ind < len(Left):
        combined.append(Left[left_ind])
        left_ind += 1

    while right_ind < len(Right):
        combined.append(Right[right_ind])
        right_ind += 1

    return combined

    # return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # What is the base case?
    # if arr size is > 1? Return.
    if len(arr) > 1:
        # Split the Array in half until there is only one value in the Array. This is the base case.
        # Sort then Add elements to the right
        left = merge_sort(arr[0:len(arr)//2])
        # Sort then Add elements to the left
        right = merge_sort(arr[len(arr)//2:])

        # merge left and right
        arr = merge(left, right)
    return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists
# # or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
