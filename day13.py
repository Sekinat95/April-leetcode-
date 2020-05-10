

# def findMaxLength(nums):
#     subarrs = allSubArrays(nums)
#     # print(subarrs)
#     evenArrs = []
#     for i in range(len(subarrs)):
#         if subarrs[i].count(0)==subarrs[i].count(1):
#             evenArrs.append(subarrs[i])
#     maxsumArr = []
#     currentsumArr = evenArrs[0]
#     for i in range(len(evenArrs)):
#         if len(evenArrs[i]) > len(currentsumArr):
#             maxsumArr = evenArrs[i]
#         else:
#             maxsumArr = currentsumArr
#     print("printing even arrays")
#     print(evenArrs)
#     print(maxsumArr)
#     return len(maxsumArr)      
    
# def allSubArrays(L,L2=None):
#     if L2==None:
#         L2 = L[:-1]
#     if L==[]:
#         if L2==[]:
#             return []
#         return allSubArrays(L2,L2[:-1])
#     return [L]+allSubArrays(L[1:],L2)

# print(findMaxLength([0,0,1,0,0,0,1,1]))

# def getAllWindows(L):
#     for w in range(1, len(L)+1):
#         for i in range(len(L)-w+1):
#             yield L[i:i+w] 

# def findMaxLength(nums):
#     dict = {0:-1}
#     subarr, count = 0,0
#     for i in range(len(nums)):
#         if nums[i] == 1:
#             count+=1
#         else:
#             count-= 1
#         if count == 0:
#             subarr = i+1
#         if count in dict:
#             max(subarr, i-dict[count])
#         else:
#             dict[count] = i
#     return subarr


def findMaxLength( nums):
    c,d,m = 0,{0:-1},0
    for key,value in enumerate(nums):
        c += 2*value -1
        if c in d:
            m = max(m,key-d[c])
        else:
            d[c] = key               
    return m 

# def findMaxLength(nums):
#     c,d,m = 0,{0:0},0
#     for i,v in enumerate(nums):
#         c += 2*v -1
#         if c in d:
#             m = max(m,i+1-d[c])
#         else:
#             d[c] = i+1                
#     return m

print(findMaxLength([0,0,1,0,0,1,1]))
