# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if current l1 node is null then list1 has ended and you can return the rest of list2
        if list1 is None:
            return list2
        #if current l2 node is null then list2 has ended and you can return the rest of list1
        elif list2 is None:
            return list1
        
        elif list1.val < list2.val:
            #if the current l1 node val is less than l2 then the next node will either be 
            #l1.next or an l2 node
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            #if the current l1 node val is less than l2 then the next node will either be 
            #l1.next or an l2 node
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
