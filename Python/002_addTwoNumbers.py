'''
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Related topics: Linked list, Math

Similar questions: Multiply strings, Add Binary
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def add(self, curNode, addNode):
        addNode.next = curNode
        curNode = addNode
        return curNode
        

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next

if __name__ == '__main__':
    # Generate two linked-list
    l1 = ListNode(3)
    l1 = l1.add(l1, ListNode(4))
    l1 = l1.add(l1, ListNode(2))
    l2 = ListNode(4)
    l2 = l2.add(l2, ListNode(6))
    l2 = l2.add(l2, ListNode(5))
    # Solution of addTwoNumbers
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    while res != None:
        if res.next == None:
            print(res.val)
        else:
            print(res.val, "->", end=" ")
        res = res.next
    