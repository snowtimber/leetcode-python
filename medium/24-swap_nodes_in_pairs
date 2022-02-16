'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        print(dummy)
        dummy.next = head
        print(dummy.next)
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next

            #assign nexts cur current, first, and 2nd nodes
            cur.next = sec
            first.next = sec.next
            sec.next = first

            #does assigning cur.nex.next to cur lock it in to the dummy?
            cur = cur.next.next
            print(cur)
            print(dummy)
            print(dummy.next)

        return dummy.next

'''
class Solution(object):
def swapPairs(self, head):
    if not head or not head.next: return head
    new_start = head.next.next
    head, head.next = head.next, head
    head.next.next = self.swapPairs(new_start)
    return head
'''
