#max sub array
def maxSubArray(nums):

    #newnums = list(nums)
    currentSum = maxsum = nums[0]
       
    #subarrsum = 0
    for i in range(1,len(nums)):
        
        currentSum = max(currentSum+nums[i], nums[i])
        maxsum = max(currentSum, maxsum)
    return maxsum
    
#     subarrsum = 0
#     for i in range(len(newnums)):
#         if len(newnums)>8:
            
#             newsubarrsum = sum(newnums[i:i+4])
#             if newsubarrsum>subarrsum:
#                 subarrsum = newsubarrsum
#         else:
#             newsubarrsum = sum(newnums[i:i+2])
#             if newsubarrsum>subarrsum:
#                 subarrsum = newsubarrsum
#     print(subarrsum)
#     return subarrsum
            

maxSubArray([1,2,3,4,5,6,7,8])