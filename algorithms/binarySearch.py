"""
Binary search works on sorted arrays. Binary search begins by comparing the middle element 
of the array with the target value. If the target value matches the middle element, 
its position in the array is returned. If the target value is less than the middle element, 
the search continues in the lower half of the array. If the target value is greater than the 
middle element, the search continues in the upper half of the array.

O(log N)
"""
import math

def binarySearch(sortedArray,target):
    left=0
    right=len(sortedArray) - 1
    while left <= right:
        middle = math.floor((left + right) / 2)
        if sortedArray[middle] < target:
            left = middle + 1
        else:
            if sortedArray[middle] > target:
                right = middle - 1
            else:
                return middle
    return -1


a=[1,2,3,4,5,6,7,8,9,10,11,12]
print(binarySearch(a,9))


def search(sortedArray, v) -> bool:
    m = len(sortedArray)
    if m == 0:
        return False
    idx = m//2
    print(f"a={sortedArray[idx]} and {sortedArray} and i:{idx}")
    if sortedArray[idx] == v:
        return True
    elif sortedArray[idx] < v:
        # search in [idx+1, m]
        return search(sortedArray[idx+1:m],v)
    else:
        # search in [0, idx-1]
        return search(sortedArray[0:idx],v)
    
print(search(a,9))
