# Objectives

# Practice more complex array operations.
# Strengthen understanding of element counting and filtering.
# Begin thinking in terms of problem-solving patterns.

# 1. Remove Duplicates from an Array
# 2. Count Occurrences of Each Element
# 3. Find All Elements Appearing More Than Once

def remove_duplicates(arr):
    result = []
    myset = set()
    for element in arr:
        if element not in myset:
            myset.add(element)
            result.append(element)
    return result

print(remove_duplicates([1, 2, 2, 3, 1]))
print(remove_duplicates([4, 4, 4, 4]))

# Edge cases: empty array : empty new array is returned
# Time complexity: O(n) as find in dictionary is O(1) and parsing is O(n)
# Space complexity: O(n) as the array returned occupies space for storing maximum n elements

def count_occurrences(arr):
    mydict = {}
    for element in arr:
        mydict[element] = mydict.get(element, 0) + 1
    return mydict

print(count_occurrences([1, 2, 2, 3, 1, 3, 3]))
print(count_occurrences([5, 5, 5]))

# Edge cases: empty array : empty dictionary is returned
# Time complexity: O(n) as parsing is O(n)
# Space complexity: O(n) as the dictionary returned occupies space for storing maximum n elements

def get_repeating_elements(arr):
    result = []
    mydict = {}
    for element in arr:
        if element not in mydict:
            mydict[element] = 1
        else:
            if mydict[element] == 1:
                result.append(element)
            mydict[element] += 1
    return result

print(get_repeating_elements([1, 2, 3, 2, 3, 4]))
print(get_repeating_elements([10, 20, 30]))

# Edge cases: empty array or array with no repeating elements: empty array is returned
# Time complexity: O(n) as parsing is O(n)
# Space complexity: O(n) as the array and dictionary occupies space for storing maximum n elements
