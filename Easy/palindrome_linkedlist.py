
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        forward = ''
        node = head
        while node is not None:
            forward += str(node.val)
            node = node.next
        return forward == forward[::-1]

four = ListNode(1)
third = ListNode(2, four)
second = ListNode(2, third)
head = ListNode(1, second)

soln = Solution()
ans = soln.isPalindrome(head)
print(ans)



