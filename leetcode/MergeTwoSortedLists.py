# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        answer = cur = ListNode(0)
        if not list1 and not list2:
            return None
        elif not list1 or not list2:
            return list1 or list2
        else:
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
        cur.next = list1 or list2
        return answer.next
