# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp_dict = {}
        size = 0
        head_ref = head
        while (head_ref != None):
            temp_dict[size] = head_ref
            size += 1
            head_ref = head_ref.next

        if (size == n):
            head = head.next
        else:
            search_idx = temp_dict[size - n]
            search_prev = temp_dict[size - n - 1]
            search_prev.next = search_idx.next

        return head

    #Follow up: Could you do this in one pass?

    def removeNthFromEnd(self, head, n):
        head_ref = head
        head_ref_n = head

        for i in range(n):
            head_ref_n = head_ref_n.next
        
        while(head_ref_n is not None):
            if (head_ref_n.next is None):
                break
            else:
                head_ref = head_ref.next
                head_ref_n = head_ref_n.next
        
        if head_ref_n is None:
            head = head.next
        else:
            rm = head_ref.next
            head_ref.next = rm.next

        return head