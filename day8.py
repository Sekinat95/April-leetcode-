# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         head = x;
#     print(head)

# MIDDLE OF A LINKEDLIST
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
# 
# 
class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        
        # store data
        self.data = data
        
        # store reference (next item)
        self.next = None
        return
    
    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

    def middleNode(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            fast = slow = head
            while fast and fast.next:
                fast, slow = fast.next.next, slow.next
            return slow

mylist = ListNode([1,2,3,4])
print(mylist.has_value([1,2,3,4]))
print(mylist.middleNode([]))

