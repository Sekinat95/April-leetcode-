# def countElements(arr):
#     """
#     :type arr: List[int]
#     :rtype: int
#     """
#     for i in range(len(arr)):
#         if arr[i] + 1 in arr:
#             result = arr.count(arr[i])
#     return result

# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.
# Input: arr = [1,3,2,3,5,0]
# Output: 3
# Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr...

def countElements(arr):
    
    result =0
    for i in range(len(arr)):
        if arr[i]+1 in arr:
           result +=1
            
    return result
                            
 
    return count

# def countElements(arr):
#     ele = {}
#     for i in arr:
#         ele[i] = 1

#         result = 0
#         for x in arr:
#             if x+1 in ele:
#                 result +=1
#     return result
   

print(countElements([1,1,2,2]))
print(countElements([1,3,2,3,5,0]))