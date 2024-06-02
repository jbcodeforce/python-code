"""
Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

numbers are > 0, nums is not sorted, we can have the same number multiple times in nums

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

O(log N)
"""
from typing import List

def two_sum_O2(nums, target) -> (int, int):
    """
    brute force is to loop over the array and look at the numbers above to find
    the complement and return the first match 
    """
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return (i,j)
    return (-1,-1)
    

def two_sum(nums: List[int], target: int) -> (int, int):
    """
    loop over the list in one shot. 
    use a list of complement from current number to the target if there is no 
    one existing in the complements already
    O(log(n))
    """
    complements=[]
    for i in range(0,len(nums)):
        # do we have a complement
        comp = target-nums[i]
        for j in range(0,len(complements)):
            p_i, c = complements[j]
            if nums[i] == c:
                return (p_i,i)
        if nums[i] < target:
            complements.append((i,comp))
    return (-1,-1)

a,b= two_sum([2,7,11,15],9)

print(a,b)

print(two_sum([3,2,4],6))
print(two_sum([3,2,4],8))
print(two_sum([3,3],6))
