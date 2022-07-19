# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        num_nodes = 0
        #create a copy of the head node to traverse linked list without affected values
        dum_head = head
        #iterate through LL
        while(dum_head):
            num_nodes+=1
            dum_head = dum_head.next
        #split the array in half. If list is odd length take 2nd middle node
        num_nodes = (math.ceil(num_nodes//2))
        
        #find middle node and return
        for i in range(0,num_nodes):
            num_nodes -= 1
            head = head.next

        return head
