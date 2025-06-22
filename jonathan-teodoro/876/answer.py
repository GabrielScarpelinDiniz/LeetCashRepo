# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        answer = []
        while (curr):
            answer.append(curr)
            curr = curr.next

        mid = len(answer)//2
        return answer[mid]

            