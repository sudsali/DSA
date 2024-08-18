# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            temp = head
            l = 0 
            while temp:
                l+=1
                temp = temp.next
            print(l)
            even = head.next
            odd = head
            even_head = even
            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
            odd.next = even_head
            return head
        else:
            return None