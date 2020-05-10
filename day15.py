import math
def productExceptSelf( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = [1]*len(nums)
    prod= 1
    for i in range(len(nums)):
        #result[i] = math.prod(nums[:i])*math.prod(nums[i:])
        result[i] *=prod
        prod *= nums[i]
    prod = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= prod
        prod *= nums[i]

    return result
print(productExceptSelf([1,2,3]))