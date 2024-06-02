"""
Remove element

Given an integer array nums and an integer val, remove all occurrences of val 
in nums in-place.
The order of the elements may be changed. Then return the number of elements 
in nums which are not equal to val

nums
"""
from typing import List

def remove_element_1(nums: List[int],val: int) -> (int,List[int]):
    c=0
    for i in range(0,len(nums)):
        if nums[i] == val:
            nums[i]=None
            c+=1
    for k in range(0,len(nums)):
        if nums[k] == None:
            for j in range(k,len(nums)):
                if nums[j] != None:
                    nums[k] = nums[j]
                    nums[j] = None
                    break
    return (len(nums)-c,nums)

def remove_element(nums: List[int],val: int) -> (int,List[int]):
    c=0
    for i in range(0,len(nums)):
        if nums[i] == val:
            nums[i]= None
            for k in range(len(nums)-1,i,-1):
                if nums[k] != val and nums[k] != None:
                    nums[i]=nums[k]
                    nums[k]=None
                    break
            c+=1
    return (len(nums)-c,nums)

def better_sol(nums: List[int],val: int) -> (int,List[int]):
    """
    use index of the non target element
    """
    idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[idx]= nums[i]
            idx+=1
    return (idx,nums)

nums=[3,2,2,3]
val=3
expected_num=[2,2,None,None]

k,en = remove_element(nums,val)
print(k,en)
assert k == 2
assert expected_num == en
nums = [0,1,2,2,3,0,4,2]
val = 2
k,en = better_sol(nums,val)
print(k,en)
assert k == 5
assert en[0:k] == [0,1,3,0,4]
