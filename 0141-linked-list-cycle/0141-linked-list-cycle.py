# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        n=-1
        adress=[]
        i=0
        while(head):
            adress.append(head)
            head=head.next
            if(head in adress):
                n=i
                break
            i+=1
        return n!=-1