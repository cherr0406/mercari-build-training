# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        # Time complexity: O(n)
        # Space complexity: O(1)

        initA, initB = headA, headB

        # count length
        lenA, lenB = 0, 0
        while headA != None:  #  O(n)
            lenA += 1
            headA = headA.next
        while headB != None:  #  O(n)
            lenB += 1
            headB = headB.next

        # init variables
        headA, headB = initA, initB

        # make lenA <= lenB
        if lenA > lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        # move B's head
        for _ in range(lenB - lenA):
            headB = headB.next

        # find intersection
        while headA != None:  #  O(n)
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        # Floyd's Linked List Cycle Finding Algorithm
        # Time complexity: O(n)
        # Space complexity: O(1)

        if not (headA and headB):
            return None

        # returns the starting point of cycle
        def floydsCycleFinding(head: ListNode) -> ListNode | None:
            if head.next == None:
                return None
            slow, fast = head.next, head.next.next
            while fast != None and fast.next != None:  # O(n)
                if slow == fast:
                    while slow != head:  # max: cycle length
                        head = head.next
                        slow = slow.next
                    return head
                slow = slow.next
                fast = fast.next.next
            return None

        # put a pointer from A's tail to A's head
        ptA = headA
        while ptA.next != None:  #  O(n)
            ptA = ptA.next
        ptA.next = headA

        intersection = floydsCycleFinding(headB)
        ptA.next = None
        return intersection

    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        # less steps 2 pointers
        # Time complexity: O(n)
        # Space complexity: O(1)

        if not (headA and headB):
            return None

        ptA, ptB = headA, headB

        # make 2 linked list A-B and B-A
        # if there is a intersection, it is ptA where ptA == ptB
        # if not, finally ptA == ptB == null
        while ptA != ptB:
            if not ptA:
                ptA = headB
            else:
                ptA = ptA.next
            if not ptB:
                ptB = headA
            else:
                ptB = ptB.next

        return ptA
