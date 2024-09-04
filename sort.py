'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

'''
nums = [0,2,2,1,1,2]

def partition(arr, low, high):
    pivot = arr[high]  # Pivot can be the last element
    print ("pivot=", pivot)
    i = low - 1  # Index of smaller element
    print ("i=", i)
    print ("range low, hight=", low, high)
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        print ("i, j in range low, hight=",i, j, low, high)
        if arr[j] <= pivot:
            i += 1
            print (f"swapping {arr[i]}, {arr[j]} = {arr[j]}, {arr[i]}")
            arr[i], arr[j] = arr[j], arr[i]  # Swap
        print ("arr=", arr)

    # Swap the pivot element with the element at i+1
    print (f"swapping pivot {arr[i+1]}, {arr[high]} = {arr[high]}, {arr[i+1]}")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print ("returning i+1", i+1)
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Example usage
nums = [0, 2, 2, 1, 1, 2]
quicksort(nums, 0, len(nums) - 1)
print("Sorted array:", nums)


