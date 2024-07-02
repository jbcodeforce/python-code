"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def duplicate_in(nums)-> bool:
    # Use an array to keep encountered values
    encounters = []
    for i in nums:
        if i not in encounters:
            encounters.append(i)
        else:
            return True
    return False

assert duplicate_in([1,2,3,1])

assert not duplicate_in([1,2,3,4])

assert duplicate_in([1,1,1,3,3,4,3,2,4,2])
