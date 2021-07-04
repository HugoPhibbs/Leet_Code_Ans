class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Base cases
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            temp = l1
            l1 = l1.next
        else:
            temp = l2
            l2 = l2.next

        head = temp
        curr_node = temp

        while l1 is not None or l2 is not None:
            if l1 is None:
                temp = l2
                l2 = l2.next
            elif l2 is None:
                temp = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            curr_node.next = temp
            curr_node = curr_node.next
        return head

soln = Solution()
l1 = ListNode(1,
              ListNode(2,
                       ListNode(4, None)))
l2 = ListNode(1,
              ListNode(3,
                       ListNode(4, None)))

ans = soln.mergeTwoLists(l1, l2)
curr = ans
while curr is not None:
    print(curr.val)
    curr = curr.next
