'''
Given a sorted array of n integers and a target value,
determine if the target exists in the array in logarithmic time using the binary search algorithm.
If target exists in the array, return the index of it, else return -1.
'''


def binary_search(arr, target):
    minimum, maximum = 0, len(arr) - 1
    mid_index = (minimum + maximum) // 2
    while mid_index < len(arr) - 1:
        if arr[mid_index] == target:
            return mid_index
        elif arr[mid_index] < target:
            minimum = mid_index + 1
        else:
            maximum = mid_index - 1
        mid_index = (minimum + maximum) // 2
    return -1


# https://medium.com/techie-delight/top-25-algorithms-every-programmer-should-know-373246b4881b

