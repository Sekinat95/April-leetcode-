#Given a non-empty array of integers, 
# every element appears twice except for one.
#  Find that single one.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_dup_num = []
        
        for i in nums:
            if i not in no_dup_num:
                no_dup_num.append(i)
            else:
                no_dup_num.remove(i)
        return no_dup_num.pop()