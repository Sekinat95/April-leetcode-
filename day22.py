def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    sumdict = {0:1}
    n = len(nums)
    count = 0
    s = 0

    for num in nums:
        s+=num #cumulative sum
        if s-k in sumdict:
            count+=sumdict[s-k]
        if s in sumdict:
            sumdict[s]+=1
        else:
            sumdict[s]=1
    return count

print(subarraySum([1,1,1],2))
