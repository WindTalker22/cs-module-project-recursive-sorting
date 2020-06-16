# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=0, end=None):
    # If end is equal to None
    if end is None:
        # We assign end to equal the end
        end = len(arr) - 1
    if start > end:
        return -1

    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    return binary_search(arr, target, mid + 1, end)

# Find out if a key x exists in the sorted list
# A[left..right] or not using binary search algorithm
# def binary_search(A, left, right, x):

#     # Base condition (search space is exhausted)
#     if left > right:
#         return -1

#     # we find the mid value in the search space and
#     # compares it with key value

#     mid = (left + right) // 2

#     # overflow can happen. Use below
#     # mid = left + (right - left) / 2

#     # Base condition (key value is found)
#     if x == A[mid]:
#         return mid

#     # discard all elements in the right search space
#     # including the mid element
#     elif x < A[mid]:
#         return binary_search(A, left, mid - 1, x)

#     # discard all elements in the left search space
#     # including the mid element
#     else:
#         return binary_search(A, mid + 1, right, x)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


# def agnostic_binary_search(arr, target):
#     # Your code here
#     pass
