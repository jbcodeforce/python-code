"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

what is a subarray? it can be the array itself, or contiguous number from 1 to n elements
n <= len(array)

Given nums = [-2,1,-3,4,-1,2,1,-5,4]
sub_array=[-2]  sum=-2
sub_array=[-2,1]  sum=-1
sub_array=[-2,1,-3]
sub_array=[4,-1,2,1] sum=6 will be the biggest
"""


def sum_array(nums: []) -> int:
    """
    return the sum of the int within the given array
    """
    sum = 0
    for i in nums:
        sum+=i
    return sum

def build_sub_array(nums: [],i,j)-> []:
    return nums[i:j]

def max_subarray(nums: []) -> int:
    """
    brut force method, build the contiguous sub array, compute the sum of sub array and
    compare to the current max
    """
    max = -10000
    subarray=[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)+1):
            s_a=build_sub_array(nums,i,j)
            sum_s_a=sum_array(s_a)
            if sum_s_a> max:
                max = sum_s_a
                subarray=s_a 
    return (subarray,max)

def better_sol(nums: []) -> int:
    """
    For O(n) we need one loop and when current sum is < 0 then we change sub array
    """
    max = -10000
    current_sum =0
    subarray=[]
    new_idx=0
    for i in range(0,len(nums)):
        current_sum +=nums[i]
        if current_sum < 0:
            current_sum = 0
            subarray=[]
            new_idx=i+1
        else:
            if current_sum > max:
                max=current_sum
                subarray=nums[new_idx:i+1]

    return (subarray,max)

nums=[-2,1,-3,4,-1,2,1,-5,4]

print(max_subarray(nums))
assert ([4, -1, 2, 1], 6) == max_subarray(nums)
print(max_subarray([1]))
print(max_subarray([5,4,-1, 7, 8]))
print(better_sol(nums))