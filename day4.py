# def moveZeroes( nums):

#     """
#     :type nums: List[int]
#     :rtype: None Do not return anything, modify nums in-place instead.
#     """
#     #l.insert(newindex, l.pop(oldindex))
#     print("hello") 
#     for i in range(len(nums)):
#         if nums[i]==0:
#            nums.insert(len(nums)-1,nums.pop(i))
#         

#     print(nums)

#**********************
# Given an array nums, write a function 
# to move all 0's to the end of it while
#  maintaining the relative order of the non-zero elements.

def moveZeroes( nums):

    num_zeros = nums.count(0)
    print(num_zeros)
    for n in range(num_zeros):
          # repeat until all zeros are shifted to the end
        for i in range(len(nums)-1):

            if nums[i]==0:

                nums[i],nums[i+1]=nums[i+1],nums[i]

    print(nums)
    
   



moveZeroes([0,4,5,0,1,9,0])