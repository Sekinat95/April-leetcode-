# def lastStoneWeight( stones):
#     """
#     :type stones: List[int]
#     :rtype: int
#     """
#     print(stones)
#     while(len(stones)==1):
#         return stones[0]
#     x,y = maxList(stones)
#     print(stones)
#     if x==y:
#         stones.remove(x)
#         stones.remove(y)

        
#     elif x!=y:
#         stones
#         stones.append(y-x)
#         stones.remove(x)
#         stones.remove(y)
        
        


# def maxList(list):
#     listcopy = list.copy()
#     #print(listcopy)
#     y = max(list)
#     y_index = list.index(y)
#     list.pop(y_index)
#     x = max(list)
#     return x,y

# print(maxList([2,7,4,1,8,1])) 
# print(lastStoneWeight([2,7,4,1,8,1]))


# *****************************
# We have a collection of stones, each stone has a positive integer weight.
# Each turn, we choose the two heaviest stones and smash them together.  
# Suppose the stones have weights x and y with x <= y.  The result of this smash is:
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

def lastStoneWeight(stones):
    while len(stones)>1:
        stones.sort()
        if stones[-1]==stones[-2]:
            stones = stones[:-2]
        elif stones[-1]!=stones[-2]:
            stones[-2] = stones[-1] - stones[-2]
            stones = stones[:-1]
    if len(stones)==1:
        return stones[0]
    else:
        return 0
print(lastStoneWeight([2,7,4,1,8,1]))
