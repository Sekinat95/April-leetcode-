def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        
        for i in nums:
            if i == target:
                return nums.index(target)
    else:
        return -1
