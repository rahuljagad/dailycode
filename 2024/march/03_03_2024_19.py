'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head
        position = 0
        while front != None:
            front = front.next
            if position > n:
                back = back.next
            position += 1
        if position <= n:
            if back == head:
                head = head.next
        else:
            if back and back.next:
                back.next = back.next.next
        return head
