# Objectives

#Understand array basics: indexing, iteration, modification.
#Learn to manipulate elements using loops.
#Practice basic time/space complexity analysis.

# 1. Find Maximum Number in Array
# 2. Reverse an Array In-Place
# 3. Return Indices of Even Numbers

def get_max_array(arr):
    if len(arr) == 0:
        return None
    result = arr[0]
    for i in arr[1:]:
        result = max(result, i)
    return result

print(get_max_array([3, 5, 1, 2, 4]))
print(get_max_array([-10, -3, -1, -7]))

# Edge cases: when array is empty, returns None
# Time complexity : O(n) , n is the array length
# Space complexity : O(1) , extra space only to store result

def reverse_array_inplace(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]

arr1 = [1, 2, 3, 4, 5]
reverse_array_inplace(arr1)
print(arr1)
arr2 = [7, 8]
reverse_array_inplace(arr2)
print(arr2)

# Edge cases: when array is empty, its automatically handled by length
# Time complexity : O(n) , n is the array length
# Space complexity : O(1) , reverse in place, no extra space required

def get_indices_even_numbers(arr):
    result = []
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            result.append(i)
    return result

print(get_indices_even_numbers([1, 4, 2, 7, 10]))
print(get_indices_even_numbers([3, 5, 7]))

# Edge cases: when array is empty, empty array is returned
# Time complexity: O(n), n is the array length
# Space complexity: O(n), to store indices of even numbers to return
